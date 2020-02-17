#!/usr/bin/env python
# coding=utf-8

import rospy
from temizlik_robotu_servis_istemci_ornek.srv import *


class TemizlikRobotuIstemciOrnek(object):
    def __init__(self):
        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        # Servise gönderilecek isteği tutan değişken
        gonderilecek_istek = "Gorev Yuzdesi"

        # İstemci fonksiyonunu çağırarak servise gönderilmek istenen istek gönderilir.
        # servisten_gelen_yanit değerine Serviste yapılan işlem sonucu yanıt değeri dönmektedir.
        servisten_gelen_yanit = self.bilgi_servisi_ornek_istemcisi(gonderilecek_istek)
        print("Servisten Gelen Yanit")
        print("\nTamamlanan Gorev Yuzde Degeri = % " + str(servisten_gelen_yanit) + "\n\n")


    def bilgi_servisi_ornek_istemcisi(self, istek):
        rospy.wait_for_service('bilgi_servisi_ornek')
        try:
            # bilgi_servisi_ornek servisi ile bağlantıyı sağlamaktadır.
            bilgi_servisi_ornek = rospy.ServiceProxy('bilgi_servisi_ornek', BilgiServisiOrnek)
            # Servise isteği parametre olarak yollar ve servisin cevabı yanit olarak gelmektedir.
            yanit = bilgi_servisi_ornek.call(BilgiServisiOrnekRequest(istek))

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
