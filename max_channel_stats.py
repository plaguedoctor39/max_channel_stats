stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
def max_channel_stats(stats):
    max_stats = 0
    max_channel = ''
    for channel in stats:
        if stats[channel] > max_stats:
            max_stats = stats[channel]
            max_channel = channel
    return max_channel
print(max_channel_stats(stats))