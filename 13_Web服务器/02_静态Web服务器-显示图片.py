import socket

# 创建电话
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

tcp_server_socket.bind(("", 8080))

tcp_server_socket.listen(128)

while True:
    # 接受链接请求
    client_socket, addr = tcp_server_socket.accept()

    # 接受数据
    recv_Data = client_socket.recv(1000000)
    print(recv_Data.decode())

    # 判断客户端是否关闭
    if len(recv_Data) == 0:
        print("客户端关闭")
        break

    # 打开资源文件
    f = open("./static/index.html", "rb")
    file_data = f.read()
    f.close()

    # 响应行
    respose_line = "HTTP/1.1 200 OK\r\n"
    respose_header = "server:py1.0\r\n"
    respose_body = file_data

    respose_data = (respose_line + respose_header + "\r\n").encode() + respose_body

    # 发送数据
    client_socket.send(respose_data)
    client_socket.close()

tcp_server_socket.close()
