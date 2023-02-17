import asyncio

import requests
import tornado.web
import settings
import abc


class MainHandler(tornado.web.RequestHandler, abc.ABC):
    def get(self):
        self.render('templates/index.html')

    def post(self):
        r = requests.post('https://api.telegram.org/bot5473936156:AAElTjeR8ydJrPK57_eOF1dDEs1I9aqiBbg/sendMessage',
                      data={"chat_id": -1001854322126, 'text': f"{self.get_argument('name')} - {self.get_argument('telephone')}"})
        print(r.text)

async def main():
    app = tornado.web.Application(**settings.app_settings)
    app.add_handlers(r'.*', [
        (r'/', MainHandler)
    ])
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())