import scrapy
from ..items import PbaTeamItem
from ..items import PbaPlayersItem

class PbasipderSpider(scrapy.Spider):
    name = "pbaspider"
    allowed_domains = ["www.pba.ph"]
    start_urls = ["https://www.pba.ph/teams"]

    def parse(self, response):
        teams = response.css("div.team-page-img")

        for team in teams:
            team_url = team.css('div.team-page-img a').attrib['href']

            yield response.follow(team_url, callback=self.parse_team_page)

    def parse_team_page(self,response):

        #extract team infos
        team_data = PbaTeamItem()
        team_data['url'] = response.url
        team_data['name'] = response.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/div[1]/div/h3/text()').get()
        team_data['coach'] = response.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/div[2]/div[1]/h5[2]/text()').get()
        team_data['manager'] = response.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/div[2]/div[1]/h5[4]/text()').get()
        team_data['logo'] = response.xpath('/html/body/div[5]/div[3]/div[1]/div/div[1]/center/img').get()

        yield team_data

        #extract player infos
        player_data = PbaPlayersItem()
        players = response.css('a.p-link')

        for data in players:
            name = data.css('h4 ::text').getall()
            name = " ".join(name).strip()
            player_data['name'] = name
            player_data['team'] = response.xpath('/html/body/div[5]/div[3]/div[1]/div/div[2]/div[1]/div/h3/text()').get()
            player_data['url'] = data.css('a').attrib['href']
            player_data['number'] = data.css('p ::text').get()
            player_data['position'] = data.css('p ::text').get()
            player_data['mugshot'] = data.css('.img-rounded').attrib['src']

            yield player_data
