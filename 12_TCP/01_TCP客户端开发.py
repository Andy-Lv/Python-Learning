import socket  # 电话

# 创建客户端套接字对象
# 参数1:ipv4    参数2:选择协议(SOCK_STREAM =>tcp协议)
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 和服务端套接字建立联接
# 参数：元组（两个元素！！！）服务器IP和服务器端口号
tcp_client_socket.connect("192.168.144.29", 8080)

# 发送数据,说话,需要发送二进制类型
# 字符串转换为二进制encode("utf-8")
# 二进制转换为字符串decode("utf-8")
tcp_client_socket.send("123".encode("utf8"))

# 接受数据,聆听
# 参数：以字节为单位的接受的数据的大小
# 注意：recv会阻塞等待数据的到来
recv_data = tcp_client_socket.recv(1024)
print(recv_data.decode("utf8"))

# 关闭客户端套接字
tcp_client_socket.close()
