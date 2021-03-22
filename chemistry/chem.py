LEVELS = ('1s', '2s', '2p', '3s',
          '3p', '4s', '3d', '4p',
          '5s', '4d', '5p', '6s',
          '4f', '5d', '6p', '7s',
          '5f', '6d', '7p')


def electron_config(electrons):
    '''
    Given the number of atom's electrons, returns its electron configuration

    Warning: 0 < electrons <= 118
    '''
    configuration = ''
    for level in (LEVELS):

        if level[1] == 's':
            elec_capacity = 2

        if level[1] == 'p':
            elec_capacity = 6

        if level[1] == 'd':
            elec_capacity = 10

        if level[1] == 'f':
            elec_capacity = 14

        if electrons - elec_capacity <= 0:
            configuration += f'{level}{electrons}'
            return configuration

        else:
            configuration += f'{level}{elec_capacity} '
            electrons -= elec_capacity
