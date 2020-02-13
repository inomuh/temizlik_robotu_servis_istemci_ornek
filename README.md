# temizlik_robotu_servis_istemci_ornek


Workspace yok ise workspace oluşturunuz.

Örn. http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Daha sonra workspace gidiniz ve paketi indiriniz.

cd <WORKSPACE_NAME>

git clone "https://github.com/inomuh/temizlik_robotu_servis_istemci_ornek.git"

cd <WORKSPACE_NAME>

catkin_make

catkin_make install

source devel/setup.bash




Servisi çalıştırmak için

$ rosrun temizlik_robotu_servis_ornek temizlik_robotu_servis_ornek_dugumu.py



İstemciyi çalıştırmak için

$ rosrun temizlik_robotu_istemci_ornek temizlik_robotu_istemci_ornek_dugumu.py
