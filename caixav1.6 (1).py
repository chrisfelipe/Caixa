import firebirdsql
from tkinter import *
from datetime import datetime


def vendas():
   
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")


   
            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.44.99.39")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for a in cur.fetchone():
                    if a == None:
                        a1 = 1
                    else:
                         a1 = a
            except:
                 a1 = 1.5
            
            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.170.202.45")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for l in cur.fetchone():
                    if l == None:
                        l1 = 1
                    else:
                         l1 = l
            except:
                 l1 = 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.248.81.80")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for b in cur.fetchone():
                    if b == None:
                        b1 = 1
                    else:
                         b1 = b
            except:
                 b1 = 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.143.11.248")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for c in cur.fetchone():
                    if c == None:
                        c1= 1
                    else:
                         c1 = c
            except:
                 c1 = 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.27.151.57")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for d in cur.fetchone():
                    if d == None:
                        d1 = 1
                    else:
                         d1 = d
            except:
                 d1 = 1.5
            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.85.84.235")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for e in cur.fetchone():
                    if e == None:
                        e1 = 1
                    else:
                         e1 = e
            except:
                e1 = 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.202.150.79")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for f in cur.fetchone():
                    if f == None:
                        f1 = 1
                    else:
                         f1 = f
            except:
                 f1 = 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.35.192.131")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for g in cur.fetchone():
                    if g == None:
                        g1 = 1
                    else:
                         g1 = g
            except:
                 g1= 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.120.97.65")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for m in cur.fetchone():
                    if m == None:
                         m1 = 1
                    else:
                         m1 = m   
            except:
                 m1 = 1.5

            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.86.153.62")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for h in cur.fetchone():
                    if h == None:
                        h1 = 1
                    else:
                         h1 = h
            except:
                 h1 = 1.5
            try:
                conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.237.205.67")

                cur = conn.cursor()
                cur.execute("select sum(valo) from cadnot")
                for j in cur.fetchone():
                    if j == None:
                        j1 = 1
                    else:
                         j1 = j
                
            except:
                 j1= 1.5
            conn.close() 
            tot = a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1 + j1 + m1 + l1
            if a1 == 1.5 or b1 == 1.5 or c1 == 1.5 or d1 == 1.5 or e1 == 1.5 or f1 == 1.5 or g1 == 1.5 or h1 == 1.5 or j1 == 1.5 or m1 == 1.5 or l1 == 1.5:
                 a2 = 'loja 1 Caixa fechado'
                 b2 = 'loja 5 Caixa fechado'
                 c2 = 'loja 6 Caixa fechado'
                 d2 = 'loja 7 Caixa fechado'
                 e2 = 'loja 8 Caixa fechado'
                 f2 = 'loja 9 Caixa fechado'
                 g2 = 'loja 11 Caixa fechado'
                 h2 = 'loja 13 Caixa fechado'
                 j2 = 'loja 14 Caixa fechado'
                 m2 = 'loja 16 Caixa fechado'
                 
                 vendas2 = 'ATENÇÃO POSSUI CAIXA(S) PARADOS'
                   
            else:
                 vendas2 = 'ALL WORKING'     
            vendas = f'''
        Loja      Valor
            01 :    R$ {a1:,.2f}
            ======================
            04 :    R$ {l1:,.2f}
            ======================
            05 :    R$ {b1:,.2f}
            ======================
            06 :    R$ {c1:,.2f}
            ======================
            07 :    R$ {d1:,.2f}
            ======================
            08 :    R$ {e1:,.2f}
            ======================
            09 :    R$ {f1:,.2f}
            ======================
            11 :    R$ {g1:,.2f}
            ======================
            13 :    R$ {m1:,.2f}
            ======================
            14 :    R$ {h1:,.2f}
            ======================
            16 :    R$ {j1:,.2f}
            ======================
            Total   R$ {tot:,.2f}
             ======================
              Data     {now}

            '''
            
            texto2["text"]=vendas 
            texto3["text"]= vendas2
            print(f'ultima venda loja 01 {a1:,.2f}')
            print(f'ultima venda loja 05 {b1:,.2f}')
            print(f'ultima venda loja 06 {c1:,.2f}')
            print(f'ultima venda loja 07 {d1:,.2f}')
            print(f'ultima venda loja 08 {e1:,.2f}')  
            print(f'ultima venda loja 09 {f1:,.2f}') 
            print(f'ultima venda loja 11 {g1:,.2f}') 
            print(f'ultima venda loja 13 {m1:,.2f}') 
            print(f'ultima venda loja 14 {h1:,.2f}') 
            print(f'ultima venda loja 16 {j1:,.2f}') 
            print(f'Total     R${tot:,.2f}')
            print(f'em {now}')
def vendedor1():
            
     
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.44.99.39")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '238'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '138'")
            for a in cur.fetchone():
                  if a == None:
                      vend2 = 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '057'")
            for a in cur.fetchone():
                 if a == None:
                      vend3 = 0
                 else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '004'")
            for a in cur.fetchone():
                 if a == None:
                      vend4 = 0
                 else:
                      vend4 = a
            vendas = f"""
            Nome                              Venda
            Adriana Costa                       R${vend1:,.2f}
            ===================================================
            Claudilene                         R${vend2:,.2f} 
            ===================================================
            Marilene                         R${vend3:,.2f}
            ===================================================
            Patricia                         R${vend4:,.2f}
            """
        
            
            texto2["text"]=vendas 
           
           
            print(f'em {now}')
def vendedor2():
                 
     
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.248.81.80")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '272'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '019'")
            for a in cur.fetchone():
                  if a == None:
                      vend2 = 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '020'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '186'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            cur.execute("select sum(valo) from cadnot where  vend = '274'")
            for a in cur.fetchone():
                  if a == None:
                      vend5 = 0
                  else:
                      vend5 = a
                
            vendas = f"""
            Nome                              Venda

           Wesley                            R${vend1:,.2f}
         ====================================================   
            Fabiana                          R${vend2:,.2f}
         ===================================================== 
             Janete                         R${vend3:,.2f}
         ===================================================== 
            Leiliane                        R${vend4:,.2f}
         =====================================================
           Karla                            R${vend5:,.2f}
         =====================================================
        

            """
        
            
            texto2["text"]=vendas 
           
           
            print(f'em {now}')
def vendedor3():
                 
     
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.143.11.248")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '253'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '023'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '273'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '245'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            cur.execute("select sum(valo) from cadnot where  vend = '278'")
            for a in cur.fetchone():
                  if a == None:
                      vend5 = 0
                  else:
                      vend5 = a
            
            vendas = f"""
            Nome                              Venda

           Bruno                             R${vend1:,.2f}
         ====================================================   
            Gisele                           R${vend2:,.2f}
         ===================================================== 
             Cristiane                         R${vend3:,.2f}
         ===================================================== 
            Michael                          R${vend4:,.2f}
         =====================================================
            Rosiane                          R${vend5:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas 
           
           
            print(f'em {now}')                     
def vendedor4():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.27.151.57")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '242'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '247'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '218'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '030'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            
            vendas = f"""
            Nome                              Venda

           Janaina                             R${vend1:,.2f}
         ====================================================   
           Michelle                            R${vend2:,.2f}
         ===================================================== 
            Patricia                           R${vend3:,.2f}
         ===================================================== 
            Roberto ROCK                       R${vend4:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas 
           
           
            print(f'em {now}')                     
def vendedor5():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.135.170.224")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '262'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '182'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '033'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '034'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            cur.execute("select sum(valo) from cadnot where  vend = '035'")
            for a in cur.fetchone():
                  if a == None:
                      vend5 = 0
                  else:
                      vend5 = a
            cur.execute("select sum(valo) from cadnot where  vend = '112'")
            for a in cur.fetchone():
                  if a == None:
                      vend6 = 0
                  else:
                      vend6 = a
            
            vendas = f"""
            Nome                              Venda

           Alexsandra                            R${vend1:,.2f}
         ====================================================   
           Ana carolina                           R${vend2:,.2f}
         ===================================================== 
            Ana Maria                            R${vend3:,.2f}
         ===================================================== 
           Elisangela                            R${vend4:,.2f}
         =====================================================
           Luana                           R${vend5:,.2f}
         =====================================================
           Michelle                          R${vend6:,.2f}
         =====================================================

        

            """
        
        
            
            texto2["text"]=vendas 
           
           
            print(f'em {now}')                     
def vendedor6():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.202.150.79")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '157'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '243'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '268'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '088'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            
            vendas = f"""
            Nome                              Venda

           Anderson                            R${vend1:,.2f}
         ====================================================   
           Maria rosaria                           R${vend2:,.2f}
         ===================================================== 
            Meire                          R${vend3:,.2f}
         ===================================================== 
            Vendedor 09                      R${vend4:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas 
           
           
            print(f'em {now}')                                     
def vendedor7():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.35.192.131")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '110'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '166'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '169'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '277'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            
            vendas = f"""
            Nome                              Venda

            Fatima                            R${vend1:,.2f}
         ====================================================   
           Gabriel                            R${vend2:,.2f}
         ===================================================== 
            Leticia                           R${vend3:,.2f}
         ===================================================== 
                                        R${vend4:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas 
def vendedor8():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.120.97.65")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '058'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '061'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '063'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '269'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            
            vendas = f"""
            Nome                              Venda

           Adma                              R${vend1:,.2f}
         ====================================================   
            Claudia                          R${vend2:,.2f}
         ===================================================== 
            Rosimar                        R${vend3:,.2f}
         ===================================================== 
            Valeria                          R${vend4:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas 
def vendedor9():

            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.86.153.62")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '213'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '005'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '093'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '132'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            cur.execute("select sum(valo) from cadnot where  vend = '271'")
            for a in cur.fetchone():
                  if a == None:
                      vend5 = 0
                  else:
                      vend5 = a
            
            vendas = f"""
            Nome                              Venda

           Fernanda                          R${vend1:,.2f}
         ====================================================   
            Renata                          R${vend2:,.2f}
         ===================================================== 
            Vendedor loja 14                 R${vend3:,.2f}
         ===================================================== 
           Viviane                           R${vend4:,.2f}
         =====================================================
           Sidmar                          R${vend5:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas            
def vendedor10():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.237.205.67")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '152'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '266'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '155'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '119'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            cur.execute("select sum(valo) from cadnot where  vend = '246'")
            for a in cur.fetchone():
                  if a == None:
                      vend5 = 0
                  else:
                      vend5 = a
            cur.execute("select sum(valo) from cadnot where  vend = '168'")
            for a in cur.fetchone():
                  if a == None:
                      vend6 = 0
                  else:
                      vend6 = a
            cur.execute("select sum(valo) from cadnot where  vend = '076'")
            for a in cur.fetchone():
                  if a == None:
                      vend7 = 0
                  else:
                      vend7 = a
            
            vendas = f"""
            Nome                              Venda

            Estefane                        R${vend1:,.2f}
         ====================================================   
            Jessica                       R${vend2:,.2f}
         ===================================================== 
            Junho Almelindo              R${vend3:,.2f}
         ===================================================== 
           Patricia                          R${vend4:,.2f}
         =====================================================
          Rosyanne                         R${vend5:,.2f}
         =====================================================
          Justelina                        R${vend6:,.2f}
         =====================================================
          Sonia                          R${vend7:,.2f}
         =====================================================
        

            """
        
        
            
            texto2["text"]=vendas                                               
def vendedor11():
            data_e_hora_atuais = datetime.now()
            now = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

            sp = []
            ds = []
            c= 0
            conn = firebirdsql.connect(user="SYSDBA",password = "masterkey",database="C:\MVTecnologia\MVLoja\Silv.fdb",host="26.170.202.45")

            cur = conn.cursor()
            cur.execute("select sum(valo) from cadnot where  vend = '032'")
            for a in cur.fetchone():
                  if a == None:
                      vend1 = 0
                  else:
                      vend1 = a
            cur.execute("select sum(valo) from cadnot where  vend = '106'")
            for a in cur.fetchone():
                  if a == None:
                      vend2= 0
                  else:
                      vend2 = a
            cur.execute("select sum(valo) from cadnot where  vend = '275'")
            for a in cur.fetchone():
                  if a == None:
                      vend3 = 0
                  else:
                      vend3 = a
            cur.execute("select sum(valo) from cadnot where  vend = '268'")
            for a in cur.fetchone():
                  if a == None:
                      vend4 = 0
                  else:
                      vend4 = a
            cur.execute("select sum(valo) from cadnot where  vend = '279'")
            for a in cur.fetchone():
                  if a == None:
                      vend5 = 0
                  else:
                      vend5 = a

            vendas = f"""
            Nome                              Venda

            Aline                       R${vend1:,.2f}
         ====================================================   
            Kenia                      R${vend2:,.2f}
         ===================================================== 
            Marcela                    R${vend3:,.2f}
         ===================================================== 
           Meire                        R${vend4:,.2f}
         =====================================================
          Tatiana                         R${vend5:,.2f}
         =====================================================
        
        

            """
        
        
            
            texto2["text"]=vendas                              
#iniciando a interface grafica
janela = Tk()
janela.title("Christyan Real Time Sales v1.6 **Loja 04 adicionada** ")
texto = Label(janela, text="LM Vendas em tempo Real Developer Christyan Caso Apareça R$ 1,00 seria o caixa fechado é R$ 1,50 se estiver desligado ou sem internet ")
texto.grid(column= 0,row = 0,padx=10, pady=10)


botao = Button(janela, text="Buscar/Atualizar Vendas", command=vendas)
botao2 = Button(janela, text="Vendedores lj 1", command=vendedor1)
botao12 = Button(janela, text="Vendedores lj 4", command=vendedor11)
botao3 = Button(janela, text="Vendedores lj 5", command=vendedor2)
botao4 = Button(janela, text="Vendedores lj 6", command=vendedor3)
botao5 = Button(janela, text="Vendedores lj 7", command=vendedor4)
botao6 = Button(janela, text="Vendedores lj 8", command=vendedor5)
botao7 = Button(janela, text="Vendedores lj 9", command=vendedor6)
botao8 = Button(janela, text="Vendedores lj 11", command=vendedor7)
botao9 = Button(janela, text="Vendedores lj 13", command=vendedor8)
botao10 = Button(janela, text="Vendedores lj 14", command=vendedor9)
botao11 = Button(janela, text="Vendedores lj 16", command=vendedor10)

texto2 =Label(janela,text="Aguardando comando")
texto3 =Label(janela,text="Verificando Status", bg ='red', fg='black')



texto2.grid(column=0, row=3,padx=0, pady=10)
texto3.grid(column=0, row=4,padx=0, pady=0)

botao.grid(column=0,row=1,padx=1, pady=1)
botao2.grid(column=1,row=1,padx=1, pady=1)
botao3.grid(column=1,row=2,padx=1, pady=1)
botao4.grid(column=1,row=3,padx=1, pady=1)
botao5.grid(column=1,row=4,padx=1, pady=1)
botao6.grid(column=1,row=5,padx=1, pady=1)
botao7.grid(column=1,row=6,padx=1, pady=1)
botao8.grid(column=1,row=7,padx=1, pady=1)
botao9.grid(column=1,row=8,padx=1, pady=1)
botao10.grid(column=1,row=9,padx=1, pady=1)
botao11.grid(column=1,row=10,padx=1, pady=1)
botao12.grid(column=1,row=11,padx=1, pady=1)



janela.mainloop()

            




        
