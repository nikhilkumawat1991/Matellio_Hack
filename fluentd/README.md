## Installation Steps
sudo apt install ruby-dev

sudo apt install build-essential

sudo gem install fluentd -v "~> 0.12.0"

sudo fluent-gem install fluent-plugin-td

sudo gem install fluent-plugin-json

sudo fluentd --setup /etc/fluent
sudo vi /etc/fluent/fluent.conf



## Run fluentd with Azure credentials

sudo fluentd -c /etc/fluent/fluent.conf


## Install azure blob python dependencies

pip install azure-storage-blob --pre
