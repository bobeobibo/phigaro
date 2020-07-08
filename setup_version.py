# change version:
# 	readme
# 	setup
# 	latest_version.txt
# 	version file

from copy import deepcopy

setup_file = 'setup.py'
version_file = 'phigaro/_version.py'
readme_file = 'README.md'
latest_version_file = 'test_data_gitaction/latest_version.txt'
tag_file = 'tag_name'

with open(setup_file, 'r') as f:
    tmp_version = f.readlines()[12].strip()
print('Temporary %s' % tmp_version)

tmp_version = (
    tmp_version.replace('version=', '').replace('"', '').replace(',', '')
)
tmp_version = tmp_version.split('.')
version_variants = []
for i in list(range(len(tmp_version)))[::-1]:
    tmp_version_ = deepcopy(tmp_version)
    tmp_version_[i] = str(int(tmp_version_[i]) + 1)
    version_variants.append('.'.join(tmp_version_))
    tmp_version[i] = '0'


def ask_version(version_variants):
    def confirm(version, version_variants):
        print('Do you agree? Yes/No')
        user_answer = input()
        if user_answer.upper() in {'Y', 'YES'}:
            return version
        elif user_answer.upper() in {'N', 'NO'}:
            return ask_version(version_variants)
        else:
            confirm(version, version_variants)

    for i, version in enumerate(version_variants):
        print('[%d] %s' % (i, version))
    print('[%d] Type your version' % (len(version_variants)))
    user_answer = input()
    try:
        version = version_variants[int(user_answer)]
    except:
        version = user_answer
    print()
    print('You choose version: %s' % version)
    return confirm(version, version_variants)


version = ask_version(version_variants)

for file_ in [setup_file, version_file]:
    with open(file_, 'r') as f:
        lines = f.readlines()
    lines_new = []
    for line in lines:
        if ('version="' in line) or ('__version__' in line):
            line = '='.join(line.split('=')[:-1] + ['"%s",' % version])
            if '__version__' in line:
                line = line[:-1]
            line = line + '\n'
        lines_new.append(line)
    with open(file_, 'w') as f:
        f.write(''.join(lines_new))

with open(readme_file, 'r') as f:
    lines = f.readlines()
lines[0] = '# Phigaro v%s\n' % version
with open(readme_file, 'w') as f:
    f.write(''.join(lines))

with open(latest_version_file, 'w') as f:
    f.write(
        'https://github.com/bobeobibo/phigaro/raw/master/dist/phigaro-%s.tar.gz'
        % version
    )


with open(tag_file, 'w') as f:
    f.write('v%s' % version)
