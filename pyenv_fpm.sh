set -e

PYTHON_VERSION="2.7.10"
PKG=prettypublictest

SCRIPT_DIR=$(dirname $0)

# For now, travis can install these
# apt-get -y install git gcc zlib1g-dev libreadline-dev libbz2-dev libsqlite3-dev libssl-dev ruby-dev libmysqlclient-dev openssl zlib1g libreadline6 libsqlite3-0

git clone https://github.com/yyuu/pyenv-installer
( cd pyenv-installer; bin/pyenv-installer )

echo '# Load pyenv automatically by adding' > ~/.bash_profile
echo '# the following to ~/.bash_profile:' >> ~/.bash_profile

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

. .bash_profile
pyenv install $PYTHON_VERSION
pyenv virtualenv $PYTHON_VERSION $PKG
pyenv global $PKG

( cd $SCRIPT_DIR ;
  pip install ./prettypublictest )

PKG_VER=$(python -c "exec(open('$SCRIPT_DIR/$PKG/$PKG/version.py').read()); print(__version__)")


# gem install fpm
fpm -d libmysqlclient-dev \
    -d openssl \
    -d zlib1g \
    -d libreadline6 \
    -d libsqlite3-0 \
    -v $PKG_VER \
    -n $PKG-$PYTHON_VERSION \
    -s dir \
    -t deb \
    $PWD/.bash_profile $PWD/.pyenv
