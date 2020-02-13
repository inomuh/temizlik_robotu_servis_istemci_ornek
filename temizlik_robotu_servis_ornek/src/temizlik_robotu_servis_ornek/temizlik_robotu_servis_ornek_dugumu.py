#!/usr/bin/env python
# coding=utf-8

import rospy
from temizlik_robotu_servis_istemci_ornek_msgs.srv import *


class TemizlikRobotuServisOrnek(object):
    def __init__(self):
        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        self.ornek_servis = rospy.Service('ornek_servis', OrnekServis, self.ornek_servis_fonksiyonu)
        
        rospy.spin()


    def ornek_servis_fonksiyonu(self, istek):
        # İstemciden gelen istekleri geçici değişkenine aktararak işlem yapmaktadır.
        print("\n\n")
        print("Istemciden istekler geldi...")
        print("1. Istek -> " + str(istek.istek_1))
        print("2. Istek -> " + str(istek.istek_2))
        gecici_degisken = istek.istek_1 ** istek.istek_2
        print("\n")
        print("Us alma islemi gerceklesiyor...")
        print("Sonuc = " + str(gecici_degisken))
        print("\n\nIstemciye yanit olarak gonderildi...\n\n")
        # Yanıt olarak istemciye okunan değer tekrar gönderilir.
        yanit = gecici_degisken

        return OrnekServisResponse(yanit)


if __name__ == '__main__':
    try:
        rospy.init_node('temizlik_robotu_servis_ornek_dugumu', anonymous=True)

        # TemizlikRobotuServisOrnek() sınıfını çağırmaktadır.
        dugum = TemizlikRobotuServisOrnek()

    except rospy.ROSInterruptException:
        pass
