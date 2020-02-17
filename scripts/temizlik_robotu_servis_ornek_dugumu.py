#!/usr/bin/env python
# coding=utf-8

import rospy
from temizlik_robotu_servis_istemci_ornek.srv import *
import random


class TemizlikRobotuServisOrnek(object):
    def __init__(self):
        self.ana_fonksiyon()


    def ana_fonksiyon(self):
        # bilgi_servisi_ornek servisi oluşturulmuştur. Bu servis üzerinden haberleşme sağlanmaktadır.
        # BilgiServisiOrnek haberleşmek için kullanılar srv dosyasıdır.
        # self.bilgi_servisi_ornek_fonksiyonu servis çağırılınca işlemlerin yapılacağı fonksiyondur.
        self.ornek_servis = rospy.Service('bilgi_servisi_ornek', BilgiServisiOrnek, self.bilgi_servisi_ornek_fonksiyonu)

        rospy.spin()


    def bilgi_servisi_ornek_fonksiyonu(self, istek):
        # İstemciden gelen istek olduğunda bu fonksiyona gelerek servis için belirtilen işlemlerini yapmaktadır.
        tamamlanan_gorev_yuzde_degeri = self.tamamlanan_gorev_yuzde_degeri_fonksiyonu()

        print("\n\nIstemciden istek geldi...\n")
        print("Tamamlanan Gorev Yuzde Degeri\n\t\t % " + str(tamamlanan_gorev_yuzde_degeri))
        print("\n\nIstemciye yanit olarak gonderildi...\n\n")
        # Yanıt olarak istemciye tamamlanan_gorev_yuzde_degeri gönderilir.
        yanit = tamamlanan_gorev_yuzde_degeri

        return BilgiServisiOrnekResponse(yanit)


    def tamamlanan_gorev_yuzde_degeri_fonksiyonu(self):
        # 0 ve 100 arasında rastgele float değer üretir.
        tamamlanan_gorev_yuzde_degeri = random.uniform(0, 100)

        return tamamlanan_gorev_yuzde_degeri


if __name__ == '__main__':
    try:
        rospy.init_node('temizlik_robotu_servis_ornek_dugumu', anonymous=True)

        # TemizlikRobotuServisOrnek() sınıfını çağırmaktadır.
        dugum = TemizlikRobotuServisOrnek()

    except rospy.ROSInterruptException:
        pass
