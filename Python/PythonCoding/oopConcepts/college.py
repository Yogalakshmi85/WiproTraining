class College:
    def __init__(self, ccode, cname, ccity):
        self._collegecode = ccode #protected variables (_)
        self._collegename = cname
        self._collegecity = ccity

    def welcome_message(self):
        print('Welcome Everybody !!!')

    def display_college_details(self):
        print(f'College Code: {self._collegecode} \n'
              f'College Name: 'f'{self._collegename} \n'
              f'City: {self._collegecity}')
