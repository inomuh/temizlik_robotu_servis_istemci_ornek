#!/usr/bin/env python
# coding=utf-8

import rospy
from temizlik_robotu_servis_istemci_ornek_msgs.srv import *


class TemizlikRobotuIstemciOrnek(object):
    def __init__(self):
        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        gonderilecek_istek_1 = 10.0
        gonderilecek_istek_2 = 5.0

        # İstemci fonksiyonunu çağırarak servise gönderilmek istenen istek değerleri gönderilir.
        # servisten_gelen_yanit değerine Serviste yapılan işlem sonucu yanıt değeri dönmektedir.
        servisten_gelen_yanit = self.ornek_servis_istemcisi(gonderilecek_istek_1, gonderilecek_istek_2)
        print("\n")
        print("Servisten Gelen Yanit = " + str(servisten_gelen_yanit))
        print("\n\n\n")


    def ornek_servis_istemcisi(self, istek_1, istek_2):
        rospy.wait_for_service('ornek_servis')
        try:
            # Örnek servisini bağlantıyı sağlar.
            ornek_servis = rospy.ServiceProxy('ornek_servis', OrnekServis)
            # Servise istekleri parametre olarak yollar ve servis dönüşü yanit olarak gelir.
            yanit = ornek_servis.call(OrnekServisRequest(istek_1, istek_2))

            return yanit.yanit

        except rospy.ServiceException, e:
            print "Service call failed: %s" % e


if __name__ == '__main__':
    try:
        rospy.init_node('temizlik_robotu_istemci_ornek_dugumu', anonymous=True)

        # TemizlikRobotuIstemciOrnek() sınıfını çağırmaktadır.
        dugum = TemizlikRobotuIstemciOrnek()

    except rospy.ROSInterruptException:
        pass
