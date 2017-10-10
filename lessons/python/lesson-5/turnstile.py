events_list = ['push', 'push', 'coin', 'push', 'push', 'coin', 'coin']
state = 'locked' # can be 'locked' or 'unlocked'

for event in events_list:
    if state == 'locked':
        if event == 'coin':
            state = 'unlocked'
        else:
            pass
    elif state == 'unlocked':
        if event == 'push':
            state = 'locked'
        else:
            pass
