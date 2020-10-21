from grpc.tools import protoc
protoc.main(
    (
        '',
        '-I.:/usr/local/include',
        '--python_out=.',
        '--grpc_python_out=.',
        'control_yaskawa_robot_w.proto',
    )
)
