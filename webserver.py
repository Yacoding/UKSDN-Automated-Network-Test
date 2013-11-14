import tornado.ioloop
import tornado.web
import t2h

class GroupHandler(tornado.web.RequestHandler):
    def get(self):
	f = open("test_log_groups.txt",'r')
	x = '<br>'.join(f.readlines())
	f.close()
        self.write(x)
class ConnectionsHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("test_log_connections.txt",'r')
        x = '<br>'.join(f.readlines())
        f.close()
        self.write(x)
class SpeedHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("test_log_speeds.txt",'r')
        x = '<br>'.join(f.readlines())
        f.close()
        self.write(x)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("test_log_groups.txt",'r')
        x = '<br>' + '<br>'.join(f.readlines())
        f.close()
	f = open("test_log_connections.txt",'r')
        x += '<br>' + '<br>'.join(f.readlines())
        f.close()
	f = open("test_log_speeds.txt",'r')
        x += '<br>' + '<br>'.join(f.readlines())
        f.close()
        self.write(x)
class SingleConnectionHandler(tornado.web.RequestHandler):
	def get(self,host_1,host_2):
		x = t2h.web_test(host_1,host_2)
		self.write(x[1])	


application = tornado.web.Application([
    (r"/groups", GroupHandler),
    (r"/connections", ConnectionsHandler),
    (r"/speeds", SpeedHandler),
    (r"/(.+)-(.+)", SingleConnectionHandler),
    (r"/.*", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
