# Stella Kim
# Practice Activity 2: TCP/IP and Sockets

import io


class StreamProcessor(object):
    """
    Initialize instance with a stream of digits and store as instance
    variable.  Output reads two digits at a time and adds to a running total.
    Also counts the number of two digit numbers that are added together.
    """

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        count = 0  # two-digit numbers the added together
        total = 0  # total of sums

        while count < 10 and total < 200:
            digits = self._stream.read(2)
            if len(digits) < 2:
                break

            count += 1

            n = int(digits)
            total += n

        return count


if __name__ == '__main__':
    # f = io.StringIO('234761640930110349378289194')
    f = io.StringIO('123456')
    my_stream_processor = StreamProcessor(f)
    result = my_stream_processor.process()
    print(result)
