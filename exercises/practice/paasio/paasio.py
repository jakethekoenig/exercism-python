import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def read(self, size=-1):
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self):
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        written = super().write(b)
        self._write_bytes += written
        self._write_ops += 1
        return written

    @property
    def write_bytes(self):
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(data)
        self._recv_ops += 1
        return data

    @property
    def recv_bytes(self):
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        sent = self._socket.send(data, flags)
        self._send_bytes += sent
        self._send_ops += 1
        return sent

    @property
    def send_bytes(self):
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
    def send_ops(self):
        return self._send_ops
