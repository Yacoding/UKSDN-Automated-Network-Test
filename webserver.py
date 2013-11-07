import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	f = open("test_log.txt",'r')
	x = '<br>'.join(f.readlines())
	f.close()
        self.write(x)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(6666)
    tornado.ioloop.IOLoop.instance().start()
