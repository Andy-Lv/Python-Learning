import socket
import multiprocessing


def handler_client_request(client_socket):
    """处理客户端请求"""
    while True:  # 一直接受客户消息
        # 接受数据
        client_data = client_socket.recv(1024)

        # 判断客户端关闭：
        if len(client_data) == 0:
            print("客户端关闭")
            break

        client_data = client_data.decode()
        print(client_data)

        # 发送数据
        client_socket.send("123".encode())


def main():
    # 创建服务端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 端口复用设置:作用：服务端关闭，端口立马释放
    # setsocketopt:设置socket选项
    # 参数：(socket选项列表{SOL},  地址复用,  True开启选项，False关闭选项默认不开启)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    # 参数：元组（ip,端口号）
    tcp_server_socket.bind("192.168.144.29", 8080)

    # 设置监听
    # 参数：最大监听个数,处理最大请求个数
    # 从主动套接字变成了被动套接字
    tcp_server_socket.listen(128)

    # 等待接受客户端的联接请求
    # 返回值是元组(和客户端通信的socket,客户端的地址信息)
    client_socket, client_addr = tcp_server_socket.accept()

    # 创建子进程，实现客户端多任务处理
    sub_process = multiprocessing.Process(target=handler_client_request, args=(client_socket,))
    sub_process.start()

    # handler_client_request(client_socket)  # 将发送和接受数据封装为函数实现多任务

    # 关闭套接字
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
