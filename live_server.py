from http.server import HTTPServer, BaseHTTPRequestHandler
import cv2

camera = cv2.VideoCapture(0)

class LiveHttpServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print('path=', self.path)
        
        # send image
        if self.path[0:7] == '/camera':
            self.send_response(200)
            self.send_header('Content-Type', 'image/jpeg')
            self.end_headers()
            
            _, frame = camera.read()
            print(frame.size)
            img = cv2.resize(frame, (300, 200))

            param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
            _, enc_img = cv2.imencode('.jpg', img, param)
            self.wfile.write(enc_img)
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            try:
                f = open('live.html', 'r', encoding='utf-8')
                s = f.read()
            except:
                s = 'file not found'
            self.wfile.write(s.encode('utf-8'))
        else:
            self.send_response(404)
            self.wfile.write('file not found'.encode('utf-8'))

try:
    addr = ('', 8081)
    httpd = HTTPServer(addr, LiveHttpServerHandler)
    print('start server', addr)
    httpd.serve_forever()

except KeyboardInterrupt:
    httpd.socket.close()

camera.release()

