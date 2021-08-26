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
    recv_data = client_socket.recv(1000000)
    print(recv_data.decode())

    # 判断客户端是否关闭
    if len(recv_data) == 0:
        print("客户端关闭")
        break

    # 解码
    recv_data = recv_data.decode()
    print("请求报文!!!:", recv_data)

    # 对请求报文进行切割
    path_list = recv_data.split(" ")
    print("列表!!!", path_list)

    # 请求资源路径 /index.html   /index2.html
    request_path = path_list[1]

    # 异常捕获，防止出现请求不存在的文件导致服务器崩溃
    try:
        # 打开资源文件
        f = open("./static" + request_path, "rb")
        file_data = f.read()
        f.close()
    except Exception as e:
        print("异常信息:", e)

        #显示404不存在
        respose_line = "HTTP/1.1 404 NOT FOUND\r\n"
        respose_header = "server:py1.0\r\n"
        respose_body = "not found"

        respose_data = respose_line + respose_header + "\r\n" + respose_body

        client_socket.send(respose_data)

        client_socket.close()

    else:#能够找到资源
        # 响应行
        respose_line = "HTTP/1.1 200 OK\r\n"
        respose_header = "server:py1.0\r\n"
        respose_body = file_data

        respose_data = (respose_line + respose_header + "\r\n").encode() + respose_body

        # 发送数据
        client_socket.send(respose_data)
        client_socket.close()
