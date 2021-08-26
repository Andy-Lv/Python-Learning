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
    recv_Data = client_socket.recv(10000)
    print(recv_Data.decode())

    # 判断客户端是否关闭
    if len(recv_Data) == 0:
        print("客户端关闭")
        break

    # 响应行
    respose_line = "HTTP/1.1 200 OK\r\n"
    respose_header = "server:py1.0\r\n"
    respose_body = "123"

    respose_data = respose_line + respose_header + "\r\n" + respose_body

    # 发送数据
    client_socket.send(respose_data.encode())
    client_socket.close()
