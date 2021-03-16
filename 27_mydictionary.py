urdutoenglishdict={
    'pankaa':'fan',
    'kambal':'blanket',
    'ataa':'flour',
    'qalam':'pen'
}
print('the options here avalible are:')
print(urdutoenglishdict.keys())
a=(input('Enter the word you want to translate''\n'))
print(urdutoenglishdict.get(a))