# stop iptables
service iptables stop

# stop postfix mail
service postfix stop

# modify selinux 
setenforce 0
sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config

# install development environment
yum groupinstall "Development Tools" "Server Platform Development" -y

# install require package
yum -y install vim wget lsof lftp tree ntpdate

# install epel
cd /etc/yum.repos.d
wget http://mirrors.neusoft.edu.cn/epel/epel-release-latest-6.noarch.rpm
rpm -ivh epel-release-latest-6.noarch.rpm

# ntpdate time.nist.gov
cd /var/spool/cron/
echo "*/1 * * * * /usr/sbin/ntpdate time.nist.gov > /dev/null" >> root
# ansible dbservers -m shell -a 'cd /var/spool/cron/; echo "*/1 * * * * /usr/sbin/ntpdate time.nist.gov &> /dev/null" >> root'

# 提供阿里云的时间同步服务器
ntp1.aliyun.com
ntp2.aliyun.com
ntp3.aliyun.com
ntp4.aliyun.com
ntp5.aliyun.com
ntp6.aliyun.com
ntp7.aliyun.com
