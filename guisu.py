#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:42:52 2018

@author: Pedro Mesquita
"""
ID_CAL= 100
ID_CPR = 101


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os


reload(sys)
sys.setdefaultencoding('utf8')

import wx
if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    from wx.lib.pubsub import pub
    
    

class WindowClass(wx.Dialog):

    def __init__(self):     
        wx.Dialog.__init__(self, None, title="Login") 
        
        self.basic_gui()
        
    def basic_gui(self):
        
        self.panel = wx.Panel(self)
        
        
         
        self.comando=wx.ComboBox(self.panel,6,'suplane',(100,10),(150,-1),style=wx.CB_SORT,choices=['suximage','suplane','a2b','rcslocks','sufnzero','supermute','suvelan','a2i','recast','sufrac','supgc','suvelan_nccs','argv','recip','sufwatrim','suphase','suvelan_nsel','AzimVelAn','refRealAziHTI','sufwmix','suphasevel','suvelan_uccs','b2a','refRealVTI','sufxdecon','suphidecon','suvelan_usel','bhedtopar','regrid3','sugabor','supickamp','suvibro','cellauto','replace','sugain','suplane','suvlength','copyright','resamp','sugassmann','supofilt','suwaveform','cpall','rmaxdiff','sugausstaper','supolar','suweight','cpftrend','segyclean','sugazmig','suprod','suwellrf','cshot1','segyhdrmod','sugendocs','supscontour','suwfft','cshot2','segyhdrs','suget','supscube','suwind','cshotplot','segyread','sugetgthr','supscubecontour','suwindpoly','ctrlstrip','segywrite','sugethw','supsgraph','suxcontour','cwell','setbhed','sugoupillaud','supsimage','suxcor','cwpfind','smooth2','sugoupillaudpo','supsmax','suxedit','CWPGrep','smooth3d','sugprfb','supsmovie','suxgraph','cxzco','smoothint2','suharlan','supswigb','suximage','cxzcs','spsplot','suhelp','supswigp','suxmax','cz1','stiff2vel','suhilb','suptdiff','suxmovie','cz1in','striptotxt','suhistogram','suptprod','suxpicker','dctcomp','su3dchart','suhrot','suptquo','suxwigb','dctuncomp','suabshw','suhtmath','suptsum','suzero','dirtree','suacor','suiclogfft','suput','suztot','downfort','suacorfrac','suifft','suputgthr','swapbhed','dt1tosu','suaddevent','suilog','supws','swapbytes','dzdv','suaddhead','suimp2d','suquantile','sys_arch','elacheck','suaddnoise','suimp3d','suquo','elamodel','suaddstatics','suimpedance','suradon','tableq','elaps','suagc','suinterp','suramp','tetramod','elaray','suahw','suinterpfowler','surandhw','elasyn','sualford','suintvel','surandspike','thom2hti','elatriuni','suamp','suinvvxzco','surandstat','thom2stiff','entropy','suanalytic','suinvzco3d','surange','time_now','farith','suascii','sujitter','surecip','fcat','suattributes','suk1k2filter','sureduce','transp','filetype','suazimuth','sukdmdcr','surefcon','transp3d','float2ibm','subackus','sukdmdcs','sureflpsvsh','tri2uni','ftnstrip','subackush','sukdmig2d','surelan','trimodel','ftnunstrip','suband','sukdmig3d','surelanan','trip','gbbeam','subfilt','sukdsyn2d','suremac2d','triray','gendocs','subset','sukeycount','suresamp','triseis','grm','succepstrum','sukeyword','suresstat','triso','h2b','succfilt','sukfilter','susehw','trisoplot','hti2stiff','succwt','sukfrac','sushape','triview','hudson','sucddecon','sukill','sushift','tvnmoqc','i2a','sucdpbin','suktmig2d','sushw','unglitch','ibm2float','sucentsamp','sulcthw','suslowft','uni2tri','isatty','sucepstrum','sulfaf','suslowift','unif2','kaperture','suchart','sulhead','susmgauss2','unif2aniso','las2su','suchw','sulog','susort','unisam','linrort','sucliphead','sulprime','susorty','unisam2','lookpar','suclogfft','sultt','suspecfk','updatedoc','lorenz','sucmp','sumax','suspecfx','updatedocall','makevel','sucommand','sumean','suspeck1k2','updatehead','maxdiff','suconv','sumedian','suspike','upfort','maxints','sucountkey','sumigfd','susplit','usernames','merge2','sucvs4fowler','sumigffd','sustack','utmconv','merge2v','sucwt','sumiggbzo','sustatic','merge4','sudatumfd','sumiggbzoan','sustaticB','vel2stiff','mkparfile','sudatumk2dr','sumigprefd','sustaticrrs','velconv','mrafxzwt','sudatumk2ds','sumigpreffd','sustkvel','velpert','newcase','sudgwaveform','sumigprepspi','sustolt','velpertan','normray','sudiff','sumigpresp','sustrip','verhulst','overwrite','sudipdivcor','sumigps','susum','viewer3','pause','sudipfilt','sumigpspi','suswapbytes','vplusz','pdfhistogram','sudivcor','sumigpsti','susyncz','vtlvz','percent','sudivstack','sumigsplit','susynlv','vzest','precedence','sudmofk','sumigtk','susynlvcw','weekday','prplot','sudmofkcw','sumigtopo2d','susynlvfti','psbbox','sudmotivz','sumix','susynvxz','pscontour','sudmotx','sumixgathers','susynvxzcs','wpc1comp2','pscube','sudmovz','sumute','sutaper','wpc1uncomp2','pscubecontour','sudoc','suname','sutaup','wpccompress','psepsi','sudumptrace','sunan','sutaupnmo','wpcuncompress','psgraph','suea2df','sunhmospike','sutetraray','wptcomp','psimage','suedit','sunmo','sutifowler','wptuncomp','pslabel','sueipofi','sunmo_a','sutihaledmo','wtcomp','psmanager','suenv','sunormalize','sutivel','wtuncomp','psmerge','sufbpickw','sunull','sutrcount','xgraph','psmovie','sufctanismod','suocext','sutsq','ximage','pstopdfcymk','sufdmod1','suoldtonew','suttoz','xwigb','pswigb','sufdmod2','suop','sutvband','xy2z','pswigp','sufdmod2_pml','suop2','sutxtaper','z2xyz','randvel3d','sufft','supack1','suunpack1','zap','raydata','sufilter','supack2','suunpack2','rayt2d','sufind','supad','suutm','rayt2dan','sufind2','supaste','suvcat','rcpall','suflip','supef','suvel2df'])
        
        self.comando.Bind(wx.EVT_KEY_DOWN, self.onkeypress) 
        
      
        btn5 = wx.Button(self.panel, pos=(250,10), label='?', size=(35,35))
        
        
        self.lbl1=wx.StaticText(self.panel, pos=(10,25), label='Comando:', size=(100,30))
        
        self.comando6=wx.ComboBox(self.panel,6,'',(280,10),(70,-1),style=wx.CB_SORT,choices=['','|','<','>','='])
        
        self.parametros=wx.TextCtrl(self.panel, pos=(100,70),size=(100,30))
        
        self.lbl2=wx.StaticText(self.panel, pos=(10,80), label='Parametros:', size=(100,30))
        
        
        self.comando2=wx.ComboBox(self.panel,6,'suximage',(100,120),(150,-1),style=wx.CB_SORT,choices=['suximage','suplane','a2b','rcslocks','sufnzero','supermute','suvelan','a2i','recast','sufrac','supgc','suvelan_nccs','argv','recip','sufwatrim','suphase','suvelan_nsel','AzimVelAn','refRealAziHTI','sufwmix','suphasevel','suvelan_uccs','b2a','refRealVTI','sufxdecon','suphidecon','suvelan_usel','bhedtopar','regrid3','sugabor','supickamp','suvibro','cellauto','replace','sugain','suplane','suvlength','copyright','resamp','sugassmann','supofilt','suwaveform','cpall','rmaxdiff','sugausstaper','supolar','suweight','cpftrend','segyclean','sugazmig','suprod','suwellrf','cshot1','segyhdrmod','sugendocs','supscontour','suwfft','cshot2','segyhdrs','suget','supscube','suwind','cshotplot','segyread','sugetgthr','supscubecontour','suwindpoly','ctrlstrip','segywrite','sugethw','supsgraph','suxcontour','cwell','setbhed','sugoupillaud','supsimage','suxcor','cwpfind','smooth2','sugoupillaudpo','supsmax','suxedit','CWPGrep','smooth3d','sugprfb','supsmovie','suxgraph','cxzco','smoothint2','suharlan','supswigb','suximage','cxzcs','spsplot','suhelp','supswigp','suxmax','cz1','stiff2vel','suhilb','suptdiff','suxmovie','cz1in','striptotxt','suhistogram','suptprod','suxpicker','dctcomp','su3dchart','suhrot','suptquo','suxwigb','dctuncomp','suabshw','suhtmath','suptsum','suzero','dirtree','suacor','suiclogfft','suput','suztot','downfort','suacorfrac','suifft','suputgthr','swapbhed','dt1tosu','suaddevent','suilog','supws','swapbytes','dzdv','suaddhead','suimp2d','suquantile','sys_arch','elacheck','suaddnoise','suimp3d','suquo','elamodel','suaddstatics','suimpedance','suradon','tableq','elaps','suagc','suinterp','suramp','tetramod','elaray','suahw','suinterpfowler','surandhw','elasyn','sualford','suintvel','surandspike','thom2hti','elatriuni','suamp','suinvvxzco','surandstat','thom2stiff','entropy','suanalytic','suinvzco3d','surange','time_now','farith','suascii','sujitter','surecip','fcat','suattributes','suk1k2filter','sureduce','transp','filetype','suazimuth','sukdmdcr','surefcon','transp3d','float2ibm','subackus','sukdmdcs','sureflpsvsh','tri2uni','ftnstrip','subackush','sukdmig2d','surelan','trimodel','ftnunstrip','suband','sukdmig3d','surelanan','trip','gbbeam','subfilt','sukdsyn2d','suremac2d','triray','gendocs','subset','sukeycount','suresamp','triseis','grm','succepstrum','sukeyword','suresstat','triso','h2b','succfilt','sukfilter','susehw','trisoplot','hti2stiff','succwt','sukfrac','sushape','triview','hudson','sucddecon','sukill','sushift','tvnmoqc','i2a','sucdpbin','suktmig2d','sushw','unglitch','ibm2float','sucentsamp','sulcthw','suslowft','uni2tri','isatty','sucepstrum','sulfaf','suslowift','unif2','kaperture','suchart','sulhead','susmgauss2','unif2aniso','las2su','suchw','sulog','susort','unisam','linrort','sucliphead','sulprime','susorty','unisam2','lookpar','suclogfft','sultt','suspecfk','updatedoc','lorenz','sucmp','sumax','suspecfx','updatedocall','makevel','sucommand','sumean','suspeck1k2','updatehead','maxdiff','suconv','sumedian','suspike','upfort','maxints','sucountkey','sumigfd','susplit','usernames','merge2','sucvs4fowler','sumigffd','sustack','utmconv','merge2v','sucwt','sumiggbzo','sustatic','merge4','sudatumfd','sumiggbzoan','sustaticB','vel2stiff','mkparfile','sudatumk2dr','sumigprefd','sustaticrrs','velconv','mrafxzwt','sudatumk2ds','sumigpreffd','sustkvel','velpert','newcase','sudgwaveform','sumigprepspi','sustolt','velpertan','normray','sudiff','sumigpresp','sustrip','verhulst','overwrite','sudipdivcor','sumigps','susum','viewer3','pause','sudipfilt','sumigpspi','suswapbytes','vplusz','pdfhistogram','sudivcor','sumigpsti','susyncz','vtlvz','percent','sudivstack','sumigsplit','susynlv','vzest','precedence','sudmofk','sumigtk','susynlvcw','weekday','prplot','sudmofkcw','sumigtopo2d','susynlvfti','psbbox','sudmotivz','sumix','susynvxz','pscontour','sudmotx','sumixgathers','susynvxzcs','wpc1comp2','pscube','sudmovz','sumute','sutaper','wpc1uncomp2','pscubecontour','sudoc','suname','sutaup','wpccompress','psepsi','sudumptrace','sunan','sutaupnmo','wpcuncompress','psgraph','suea2df','sunhmospike','sutetraray','wptcomp','psimage','suedit','sunmo','sutifowler','wptuncomp','pslabel','sueipofi','sunmo_a','sutihaledmo','wtcomp','psmanager','suenv','sunormalize','sutivel','wtuncomp','psmerge','sufbpickw','sunull','sutrcount','xgraph','psmovie','sufctanismod','suocext','sutsq','ximage','pstopdfcymk','sufdmod1','suoldtonew','suttoz','xwigb','pswigb','sufdmod2','suop','sutvband','xy2z','pswigp','sufdmod2_pml','suop2','sutxtaper','z2xyz','randvel3d','sufft','supack1','suunpack1','zap','raydata','sufilter','supack2','suunpack2','rayt2d','sufind','supad','suutm','rayt2dan','sufind2','supaste','suvcat','rcpall','suflip','supef','suvel2df'])
        
        self.comando2.Bind(wx.EVT_KEY_DOWN, self.onkeypress2)
        
        
        self.comando5=wx.ComboBox(self.panel,6,'',(280,120),(70,-1),style=wx.CB_SORT,choices=['','|','<','>','='])
        
        
        btn6 = wx.Button(self.panel, pos=(250,120), label='?', size=(35,35))
        
             
        self.lbl2=wx.StaticText(self.panel, pos=(10,135), label='Comando2:', size=(100,30))
                
        btn1 = wx.Button(self.panel, pos=(550,280), label='Executar', size=(60,30))
        
        btn8 = wx.Button(self.panel, pos=(610,280), label='limpar', size=(50,30))
        
        #
        
        self.lbl3=wx.StaticText(self.panel, pos=(10,230), label='Comando3:', size=(100,30))
        
        
       
        self.comando3=wx.ComboBox(self.panel,6,'suximage',(100,215),(150,-1),style=wx.CB_SORT,choices=['suximage','suplane','a2b','rcslocks','sufnzero','supermute','suvelan','a2i','recast','sufrac','supgc','suvelan_nccs','argv','recip','sufwatrim','suphase','suvelan_nsel','AzimVelAn','refRealAziHTI','sufwmix','suphasevel','suvelan_uccs','b2a','refRealVTI','sufxdecon','suphidecon','suvelan_usel','bhedtopar','regrid3','sugabor','supickamp','suvibro','cellauto','replace','sugain','suplane','suvlength','copyright','resamp','sugassmann','supofilt','suwaveform','cpall','rmaxdiff','sugausstaper','supolar','suweight','cpftrend','segyclean','sugazmig','suprod','suwellrf','cshot1','segyhdrmod','sugendocs','supscontour','suwfft','cshot2','segyhdrs','suget','supscube','suwind','cshotplot','segyread','sugetgthr','supscubecontour','suwindpoly','ctrlstrip','segywrite','sugethw','supsgraph','suxcontour','cwell','setbhed','sugoupillaud','supsimage','suxcor','cwpfind','smooth2','sugoupillaudpo','supsmax','suxedit','CWPGrep','smooth3d','sugprfb','supsmovie','suxgraph','cxzco','smoothint2','suharlan','supswigb','suximage','cxzcs','spsplot','suhelp','supswigp','suxmax','cz1','stiff2vel','suhilb','suptdiff','suxmovie','cz1in','striptotxt','suhistogram','suptprod','suxpicker','dctcomp','su3dchart','suhrot','suptquo','suxwigb','dctuncomp','suabshw','suhtmath','suptsum','suzero','dirtree','suacor','suiclogfft','suput','suztot','downfort','suacorfrac','suifft','suputgthr','swapbhed','dt1tosu','suaddevent','suilog','supws','swapbytes','dzdv','suaddhead','suimp2d','suquantile','sys_arch','elacheck','suaddnoise','suimp3d','suquo','elamodel','suaddstatics','suimpedance','suradon','tableq','elaps','suagc','suinterp','suramp','tetramod','elaray','suahw','suinterpfowler','surandhw','elasyn','sualford','suintvel','surandspike','thom2hti','elatriuni','suamp','suinvvxzco','surandstat','thom2stiff','entropy','suanalytic','suinvzco3d','surange','time_now','farith','suascii','sujitter','surecip','fcat','suattributes','suk1k2filter','sureduce','transp','filetype','suazimuth','sukdmdcr','surefcon','transp3d','float2ibm','subackus','sukdmdcs','sureflpsvsh','tri2uni','ftnstrip','subackush','sukdmig2d','surelan','trimodel','ftnunstrip','suband','sukdmig3d','surelanan','trip','gbbeam','subfilt','sukdsyn2d','suremac2d','triray','gendocs','subset','sukeycount','suresamp','triseis','grm','succepstrum','sukeyword','suresstat','triso','h2b','succfilt','sukfilter','susehw','trisoplot','hti2stiff','succwt','sukfrac','sushape','triview','hudson','sucddecon','sukill','sushift','tvnmoqc','i2a','sucdpbin','suktmig2d','sushw','unglitch','ibm2float','sucentsamp','sulcthw','suslowft','uni2tri','isatty','sucepstrum','sulfaf','suslowift','unif2','kaperture','suchart','sulhead','susmgauss2','unif2aniso','las2su','suchw','sulog','susort','unisam','linrort','sucliphead','sulprime','susorty','unisam2','lookpar','suclogfft','sultt','suspecfk','updatedoc','lorenz','sucmp','sumax','suspecfx','updatedocall','makevel','sucommand','sumean','suspeck1k2','updatehead','maxdiff','suconv','sumedian','suspike','upfort','maxints','sucountkey','sumigfd','susplit','usernames','merge2','sucvs4fowler','sumigffd','sustack','utmconv','merge2v','sucwt','sumiggbzo','sustatic','merge4','sudatumfd','sumiggbzoan','sustaticB','vel2stiff','mkparfile','sudatumk2dr','sumigprefd','sustaticrrs','velconv','mrafxzwt','sudatumk2ds','sumigpreffd','sustkvel','velpert','newcase','sudgwaveform','sumigprepspi','sustolt','velpertan','normray','sudiff','sumigpresp','sustrip','verhulst','overwrite','sudipdivcor','sumigps','susum','viewer3','pause','sudipfilt','sumigpspi','suswapbytes','vplusz','pdfhistogram','sudivcor','sumigpsti','susyncz','vtlvz','percent','sudivstack','sumigsplit','susynlv','vzest','precedence','sudmofk','sumigtk','susynlvcw','weekday','prplot','sudmofkcw','sumigtopo2d','susynlvfti','psbbox','sudmotivz','sumix','susynvxz','pscontour','sudmotx','sumixgathers','susynvxzcs','wpc1comp2','pscube','sudmovz','sumute','sutaper','wpc1uncomp2','pscubecontour','sudoc','suname','sutaup','wpccompress','psepsi','sudumptrace','sunan','sutaupnmo','wpcuncompress','psgraph','suea2df','sunhmospike','sutetraray','wptcomp','psimage','suedit','sunmo','sutifowler','wptuncomp','pslabel','sueipofi','sunmo_a','sutihaledmo','wtcomp','psmanager','suenv','sunormalize','sutivel','wtuncomp','psmerge','sufbpickw','sunull','sutrcount','xgraph','psmovie','sufctanismod','suocext','sutsq','ximage','pstopdfcymk','sufdmod1','suoldtonew','suttoz','xwigb','pswigb','sufdmod2','suop','sutvband','xy2z','pswigp','sufdmod2_pml','suop2','sutxtaper','z2xyz','randvel3d','sufft','supack1','suunpack1','zap','raydata','sufilter','supack2','suunpack2','rayt2d','sufind','supad','suutm','rayt2dan','sufind2','supaste','suvcat','rcpall','suflip','supef','suvel2df'])
        
        self.comando3.Bind(wx.EVT_KEY_DOWN, self.onkeypress3)

        
        self.comando4=wx.ComboBox(self.panel,6,'',(280,215),(70,-1),style=wx.CB_SORT,choices=['','|','<','>','='])
        
        btn7 = wx.Button(self.panel, pos=(250,215), label='?', size=(35,35))
        
        
        
        self.lbl5=wx.StaticText(self.panel, pos=(10,180), label='Parametros:', size=(100,30))
        
        self.parametros2=wx.TextCtrl(self.panel, pos=(100,170),size=(100,30))
                
        self.lbl5=wx.StaticText(self.panel, pos=(10,270), label='Linha de comando:', size=(100,60))
        
        self.linha=wx.TextCtrl(self.panel, pos=(100,280),size=(445,30))
                
        self.lbl4=wx.StaticText(self.panel, pos=(355,135), label='Arquivo:', size=(100,60))
        
        self.caminho=wx.TextCtrl(self.panel, pos=(415,125),size=(130,30))
        
        btn2 = wx.Button(self.panel, pos=(550,125), label='pesquisar', size=(100,27))
        
        
                
        self.lbl5=wx.StaticText(self.panel, pos=(355,230), label='Arquivo:', size=(100,60))
        
        self.caminho2=wx.TextCtrl(self.panel, pos=(415,220),size=(130,30))
        
        btn3 = wx.Button(self.panel, pos=(550,220), label='pesquisar', size=(100,27))
        
        
        
        
        self.lbl6=wx.StaticText(self.panel, pos=(355,20), label='Arquivo:', size=(100,60))
        
        self.caminho3=wx.TextCtrl(self.panel, pos=(415,10),size=(130,30))
        
        btn4 = wx.Button(self.panel, pos=(550,10), label='pesquisar', size=(100,27))
        
      
        btn1.Bind(wx.EVT_BUTTON, self.linhacmd)
        
        btn8.Bind(wx.EVT_BUTTON, self.limpar)
        
        btn5.Bind(wx.EVT_BUTTON, self.onhelp)
        
        btn6.Bind(wx.EVT_BUTTON, self.onhelp2)
        
        btn7.Bind(wx.EVT_BUTTON, self.onhelp3)
        
        
        
        
        btn2.Bind(wx.EVT_BUTTON, self.onfile2)
        
        btn3.Bind(wx.EVT_BUTTON, self.onfile1)
        
        btn4.Bind(wx.EVT_BUTTON, self.onfile3)
      
                
        self.SetSize((670,370))
                
        self.SetTitle('Interface Gráfica - Seismic Unix')
        
    
    def onfile1(self, event):   
    
        wildcard = "Todos os arquivos (*.*)|*.*" 
        dlg = wx.FileDialog(self, "Escolha o arquivo", os.getcwd(), "", wildcard, wx.FD_OPEN)
		
        if dlg.ShowModal() == wx.ID_OK: 
           self.caminho2.SetValue(dlg.GetPath())
                           
        dlg.Destroy() 
        
    def onfile2(self, event):   
    
        wildcard = "Todos os arquivos (*.*)|*.*" 
        dlg = wx.FileDialog(self, "Escolha o arquivo", os.getcwd(), "", wildcard, wx.FD_OPEN)
		
        if dlg.ShowModal() == wx.ID_OK: 
           self.caminho.SetValue(dlg.GetPath())
                           
        dlg.Destroy() 

         
    def onfile3(self, event):   
    
        wildcard = "Todos os arquivos (*.*)|*.*" 
        dlg = wx.FileDialog(self, "Escolha o arquivo", os.getcwd(), "", wildcard, wx.FD_OPEN)
		
        if dlg.ShowModal() == wx.ID_OK: 
           self.caminho3.SetValue(dlg.GetPath())
                           
        dlg.Destroy() 
            
    def onhelp(self, event):
      
      
        os.system('gedit /usr/local/help_su/'+(self.comando.Value)+'.txt&')
        
    def onhelp2(self, event):
      
      
        os.system('gedit /usr/local/help_su/'+(self.comando2.Value)+'.txt&')
        
    
    def onhelp3(self, event):
      
      
        os.system('gedit /usr/local/help_su/'+(self.comando3.Value)+'.txt&')
        
        
        
    def linhacmd(self, event):
        
        if (((self.comando.Value) + (self.parametros.Value) + ((self.comando2.Value)+(self.parametros.Value))+(self.caminho.Value)+((self.comando3.Value)+(self.caminho2.Value))) != ''):
            self.linha.Value=(((self.comando.Value)+(self.comando6.Value)+(self.caminho3.Value)+(self.parametros.Value) + (self.comando2.Value)+(self.comando5.Value)+(self.caminho.Value)+(self.parametros2.Value)+(self.comando3.Value)+(self.comando4.Value)+(self.caminho2.Value) )+'') 
          
        
        if ((self.linha.Value) != ''):
            
                  
            os.system(self.linha.Value+'&') 
            
            
            
            
            
            
    def limpar(self, event):

        self.linha.Value=''
        self.comando.Value=''
        self.parametros.Value=''
        self.comando2.Value=''
        self.parametros2.Value=''
        
        self.comando3.Value=''
        self.parametros.Value=''
        
        self.comando4.Value=''
        self.comando5.Value=''
        self.comando6.Value=''
        
        self.caminho.Value=''
        self.caminho2.Value=''
        self.caminho3.Value=''
    
            
    def onkeypress(self, e):
        
           
        keycode = e.GetKeyCode()
                
        if keycode == 13:    
       
        
            lista=('suximage','suplane','a2b','rcslocks','sufnzero','supermute','suvelan','a2i','recast','sufrac','supgc','suvelan_nccs','argv','recip','sufwatrim','suphase','suvelan_nsel','AzimVelAn','refRealAziHTI','sufwmix','suphasevel','suvelan_uccs','b2a','refRealVTI','sufxdecon','suphidecon','suvelan_usel','bhedtopar','regrid3','sugabor','supickamp','suvibro','cellauto','replace','sugain','suvlength','copyright','resamp','sugassmann','supofilt','suwaveform','cpall','rmaxdiff','sugausstaper','supolar','suweight','cpftrend','segyclean','sugazmig','suprod','suwellrf','cshot1','segyhdrmod','sugendocs','supscontour','suwfft','cshot2','segyhdrs','suget','supscube','suwind','cshotplot','segyread','sugetgthr','supscubecontour','suwindpoly','ctrlstrip','segywrite','sugethw','supsgraph','suxcontour','cwell','setbhed','sugoupillaud','supsimage','suxcor','cwpfind','smooth2','sugoupillaudpo','supsmax','suxedit','CWPGrep','smooth3d','sugprfb','supsmovie','suxgraph','cxzco','smoothint2','suharlan','supswigb','cxzcs','spsplot','suhelp','supswigp','suxmax','cz1','stiff2vel','suhilb','suptdiff','suxmovie','cz1in','striptotxt','suhistogram','suptprod','suxpicker','dctcomp','su3dchart','suhrot','suptquo','suxwigb','dctuncomp','suabshw','suhtmath','suptsum','suzero','dirtree','suacor','suiclogfft','suput','suztot','downfort','suacorfrac','suifft','suputgthr','swapbhed','dt1tosu','suaddevent','suilog','supws','swapbytes','dzdv','suaddhead','suimp2d','suquantile','sys_arch','elacheck','suaddnoise','suimp3d','suquo','elamodel','suaddstatics','suimpedance','suradon','tableq','elaps','suagc','suinterp','suramp','tetramod','elaray','suahw','suinterpfowler','surandhw','elasyn','sualford','suintvel','surandspike','thom2hti','elatriuni','suamp','suinvvxzco','surandstat','thom2stiff','entropy','suanalytic','suinvzco3d','surange','time_now','farith','suascii','sujitter','surecip','fcat','suattributes','suk1k2filter','sureduce','transp','filetype','suazimuth','sukdmdcr','surefcon','transp3d','float2ibm','subackus','sukdmdcs','sureflpsvsh','tri2uni','ftnstrip','subackush','sukdmig2d','surelan','trimodel','ftnunstrip','suband','sukdmig3d','surelanan','trip','gbbeam','subfilt','sukdsyn2d','suremac2d','triray','gendocs','subset','sukeycount','suresamp','triseis','grm','succepstrum','sukeyword','suresstat','triso','h2b','succfilt','sukfilter','susehw','trisoplot','hti2stiff','succwt','sukfrac','sushape','triview','hudson','sucddecon','sukill','sushift','tvnmoqc','i2a','sucdpbin','suktmig2d','sushw','unglitch','ibm2float','sucentsamp','sulcthw','suslowft','uni2tri','isatty','sucepstrum','sulfaf','suslowift','unif2','kaperture','suchart','sulhead','susmgauss2','unif2aniso','las2su','suchw','sulog','susort','unisam','linrort','sucliphead','sulprime','susorty','unisam2','lookpar','suclogfft','sultt','suspecfk','updatedoc','lorenz','sucmp','sumax','suspecfx','updatedocall','makevel','sucommand','sumean','suspeck1k2','updatehead','maxdiff','suconv','sumedian','suspike','upfort','maxints','sucountkey','sumigfd','susplit','usernames','merge2','sucvs4fowler','sumigffd','sustack','utmconv','merge2v','sucwt','sumiggbzo','sustatic','merge4','sudatumfd','sumiggbzoan','sustaticB','vel2stiff','mkparfile','sudatumk2dr','sumigprefd','sustaticrrs','velconv','mrafxzwt','sudatumk2ds','sumigpreffd','sustkvel','velpert','newcase','sudgwaveform','sumigprepspi','sustolt','velpertan','normray','sudiff','sumigpresp','sustrip','verhulst','overwrite','sudipdivcor','sumigps','susum','viewer3','pause','sudipfilt','sumigpspi','suswapbytes','vplusz','pdfhistogram','sudivcor','sumigpsti','susyncz','vtlvz','percent','sudivstack','sumigsplit','susynlv','vzest','precedence','sudmofk','sumigtk','susynlvcw','weekday','prplot','sudmofkcw','sumigtopo2d','susynlvfti','psbbox','sudmotivz','sumix','susynvxz','pscontour','sudmotx','sumixgathers','susynvxzcs','wpc1comp2','pscube','sudmovz','sumute','sutaper','wpc1uncomp2','pscubecontour','sudoc','suname','sutaup','wpccompress','psepsi','sudumptrace','sunan','sutaupnmo','wpcuncompress','psgraph','suea2df','sunhmospike','sutetraray','wptcomp','psimage','suedit','sunmo','sutifowler','wptuncomp','pslabel','sueipofi','sunmo_a','sutihaledmo','wtcomp','psmanager','suenv','sunormalize','sutivel','wtuncomp','psmerge','sufbpickw','sunull','sutrcount','xgraph','psmovie','sufctanismod','suocext','sutsq','ximage','pstopdfcymk','sufdmod1','suoldtonew','suttoz','xwigb','pswigb','sufdmod2','suop','sutvband','xy2z','pswigp','sufdmod2_pml','suop2','sutxtaper','z2xyz','randvel3d','sufft','supack1','suunpack1','zap','raydata','sufilter','supack2','suunpack2','rayt2d','sufind','supad','suutm','rayt2dan','sufind2','supaste','suvcat','rcpall','suflip','supef','suvel2df')  
        
            choices=[]
        
            new_lista=[]
       
            word=str(self.comando.GetValue())
           
            
            print word
            
         
            for i in range(len(lista)):
   
                
                if word in (lista[i]):
                    
        
                    print('---------------')
                    print(lista[i])
                    
                    new_lista.append(lista[i])
                   
            choices=new_lista
        
        
            word=str(self.comando.GetValue())
          
           
                
           
            self.comando = wx.ComboBox(self.panel,6,'',(100,10),(150,-1),style=wx.CB_SORT, choices=choices)
            self.comando.Bind(wx.EVT_KEY_DOWN, self.onkeypress)    
                
        e.Skip()
            
        
        
        
    def onkeypress2(self, e):
        
            
        keycode = e.GetKeyCode()
                
        if keycode == 13:    
            
            lista=('a2b','rcslocks','sufnzero','supermute','suvelan','a2i','recast','sufrac','supgc','suvelan_nccs','argv','recip','sufwatrim','suphase','suvelan_nsel','AzimVelAn','refRealAziHTI','sufwmix','suphasevel','suvelan_uccs','b2a','refRealVTI','sufxdecon','suphidecon','suvelan_usel','bhedtopar','regrid3','sugabor','supickamp','suvibro','cellauto','replace','sugain','suplane','suvlength','copyright','resamp','sugassmann','supofilt','suwaveform','cpall','rmaxdiff','sugausstaper','supolar','suweight','cpftrend','segyclean','sugazmig','suprod','suwellrf','cshot1','segyhdrmod','sugendocs','supscontour','suwfft','cshot2','segyhdrs','suget','supscube','suwind','cshotplot','segyread','sugetgthr','supscubecontour','suwindpoly','ctrlstrip','segywrite','sugethw','supsgraph','suxcontour','cwell','setbhed','sugoupillaud','supsimage','suxcor','cwpfind','smooth2','sugoupillaudpo','supsmax','suxedit','CWPGrep','smooth3d','sugprfb','supsmovie','suxgraph','cxzco','smoothint2','suharlan','supswigb','suximage','cxzcs','spsplot','suhelp','supswigp','suxmax','cz1','stiff2vel','suhilb','suptdiff','suxmovie','cz1in','striptotxt','suhistogram','suptprod','suxpicker','dctcomp','su3dchart','suhrot','suptquo','suxwigb','dctuncomp','suabshw','suhtmath','suptsum','suzero','dirtree','suacor','suiclogfft','suput','suztot','downfort','suacorfrac','suifft','suputgthr','swapbhed','dt1tosu','suaddevent','suilog','supws','swapbytes','dzdv','suaddhead','suimp2d','suquantile','sys_arch','elacheck','suaddnoise','suimp3d','suquo','elamodel','suaddstatics','suimpedance','suradon','tableq','elaps','suagc','suinterp','suramp','tetramod','elaray','suahw','suinterpfowler','surandhw','elasyn','sualford','suintvel','surandspike','thom2hti','elatriuni','suamp','suinvvxzco','surandstat','thom2stiff','entropy','suanalytic','suinvzco3d','surange','time_now','farith','suascii','sujitter','surecip','fcat','suattributes','suk1k2filter','sureduce','transp','filetype','suazimuth','sukdmdcr','surefcon','transp3d','float2ibm','subackus','sukdmdcs','sureflpsvsh','tri2uni','ftnstrip','subackush','sukdmig2d','surelan','trimodel','ftnunstrip','suband','sukdmig3d','surelanan','trip','gbbeam','subfilt','sukdsyn2d','suremac2d','triray','gendocs','subset','sukeycount','suresamp','triseis','grm','succepstrum','sukeyword','suresstat','triso','h2b','succfilt','sukfilter','susehw','trisoplot','hti2stiff','succwt','sukfrac','sushape','triview','hudson','sucddecon','sukill','sushift','tvnmoqc','i2a','sucdpbin','suktmig2d','sushw','unglitch','ibm2float','sucentsamp','sulcthw','suslowft','uni2tri','isatty','sucepstrum','sulfaf','suslowift','unif2','kaperture','suchart','sulhead','susmgauss2','unif2aniso','las2su','suchw','sulog','susort','unisam','linrort','sucliphead','sulprime','susorty','unisam2','lookpar','suclogfft','sultt','suspecfk','updatedoc','lorenz','sucmp','sumax','suspecfx','updatedocall','makevel','sucommand','sumean','suspeck1k2','updatehead','maxdiff','suconv','sumedian','suspike','upfort','maxints','sucountkey','sumigfd','susplit','usernames','merge2','sucvs4fowler','sumigffd','sustack','utmconv','merge2v','sucwt','sumiggbzo','sustatic','merge4','sudatumfd','sumiggbzoan','sustaticB','vel2stiff','mkparfile','sudatumk2dr','sumigprefd','sustaticrrs','velconv','mrafxzwt','sudatumk2ds','sumigpreffd','sustkvel','velpert','newcase','sudgwaveform','sumigprepspi','sustolt','velpertan','normray','sudiff','sumigpresp','sustrip','verhulst','overwrite','sudipdivcor','sumigps','susum','viewer3','pause','sudipfilt','sumigpspi','suswapbytes','vplusz','pdfhistogram','sudivcor','sumigpsti','susyncz','vtlvz','percent','sudivstack','sumigsplit','susynlv','vzest','precedence','sudmofk','sumigtk','susynlvcw','weekday','prplot','sudmofkcw','sumigtopo2d','susynlvfti','psbbox','sudmotivz','sumix','susynvxz','pscontour','sudmotx','sumixgathers','susynvxzcs','wpc1comp2','pscube','sudmovz','sumute','sutaper','wpc1uncomp2','pscubecontour','sudoc','suname','sutaup','wpccompress','psepsi','sudumptrace','sunan','sutaupnmo','wpcuncompress','psgraph','suea2df','sunhmospike','sutetraray','wptcomp','psimage','suedit','sunmo','sutifowler','wptuncomp','pslabel','sueipofi','sunmo_a','sutihaledmo','wtcomp','psmanager','suenv','sunormalize','sutivel','wtuncomp','psmerge','sufbpickw','sunull','sutrcount','xgraph','psmovie','sufctanismod','suocext','sutsq','ximage','pstopdfcymk','sufdmod1','suoldtonew','suttoz','xwigb','pswigb','sufdmod2','suop','sutvband','xy2z','pswigp','sufdmod2_pml','suop2','sutxtaper','z2xyz','randvel3d','sufft','supack1','suunpack1','zap','raydata','sufilter','supack2','suunpack2','rayt2d','sufind','supad','suutm','rayt2dan','sufind2','supaste','suvcat','rcpall','suflip','supef','suvel2df')  
        
            choices=[]
        
            new_lista=[]
       
            word=str(self.comando2.GetValue())
           
            print word
            
         
            for i in range(len(lista)):
                
                if word in (lista[i]):
                
                    print('---------------')
                    print(lista[i])
                    new_lista.append(lista[i])
                   
            choices=new_lista
          
                  
            self.comando2 = wx.ComboBox(self.panel,6,'',(100,120),(150,-1),style=wx.CB_SORT, choices=choices)
            
            self.comando2.Bind(wx.EVT_KEY_DOWN, self.onkeypress2)    
                
        e.Skip()
            
        
        
    def onkeypress3(self, e):
        
            
        keycode = e.GetKeyCode()
                
        if keycode == 13:    
            
            lista=('a2b','rcslocks','sufnzero','supermute','suvelan','a2i','recast','sufrac','supgc','suvelan_nccs','argv','recip','sufwatrim','suphase','suvelan_nsel','AzimVelAn','refRealAziHTI','sufwmix','suphasevel','suvelan_uccs','b2a','refRealVTI','sufxdecon','suphidecon','suvelan_usel','bhedtopar','regrid3','sugabor','supickamp','suvibro','cellauto','replace','sugain','suplane','suvlength','copyright','resamp','sugassmann','supofilt','suwaveform','cpall','rmaxdiff','sugausstaper','supolar','suweight','cpftrend','segyclean','sugazmig','suprod','suwellrf','cshot1','segyhdrmod','sugendocs','supscontour','suwfft','cshot2','segyhdrs','suget','supscube','suwind','cshotplot','segyread','sugetgthr','supscubecontour','suwindpoly','ctrlstrip','segywrite','sugethw','supsgraph','suxcontour','cwell','setbhed','sugoupillaud','supsimage','suxcor','cwpfind','smooth2','sugoupillaudpo','supsmax','suxedit','CWPGrep','smooth3d','sugprfb','supsmovie','suxgraph','cxzco','smoothint2','suharlan','supswigb','suximage','cxzcs','spsplot','suhelp','supswigp','suxmax','cz1','stiff2vel','suhilb','suptdiff','suxmovie','cz1in','striptotxt','suhistogram','suptprod','suxpicker','dctcomp','su3dchart','suhrot','suptquo','suxwigb','dctuncomp','suabshw','suhtmath','suptsum','suzero','dirtree','suacor','suiclogfft','suput','suztot','downfort','suacorfrac','suifft','suputgthr','swapbhed','dt1tosu','suaddevent','suilog','supws','swapbytes','dzdv','suaddhead','suimp2d','suquantile','sys_arch','elacheck','suaddnoise','suimp3d','suquo','elamodel','suaddstatics','suimpedance','suradon','tableq','elaps','suagc','suinterp','suramp','tetramod','elaray','suahw','suinterpfowler','surandhw','elasyn','sualford','suintvel','surandspike','thom2hti','elatriuni','suamp','suinvvxzco','surandstat','thom2stiff','entropy','suanalytic','suinvzco3d','surange','time_now','farith','suascii','sujitter','surecip','fcat','suattributes','suk1k2filter','sureduce','transp','filetype','suazimuth','sukdmdcr','surefcon','transp3d','float2ibm','subackus','sukdmdcs','sureflpsvsh','tri2uni','ftnstrip','subackush','sukdmig2d','surelan','trimodel','ftnunstrip','suband','sukdmig3d','surelanan','trip','gbbeam','subfilt','sukdsyn2d','suremac2d','triray','gendocs','subset','sukeycount','suresamp','triseis','grm','succepstrum','sukeyword','suresstat','triso','h2b','succfilt','sukfilter','susehw','trisoplot','hti2stiff','succwt','sukfrac','sushape','triview','hudson','sucddecon','sukill','sushift','tvnmoqc','i2a','sucdpbin','suktmig2d','sushw','unglitch','ibm2float','sucentsamp','sulcthw','suslowft','uni2tri','isatty','sucepstrum','sulfaf','suslowift','unif2','kaperture','suchart','sulhead','susmgauss2','unif2aniso','las2su','suchw','sulog','susort','unisam','linrort','sucliphead','sulprime','susorty','unisam2','lookpar','suclogfft','sultt','suspecfk','updatedoc','lorenz','sucmp','sumax','suspecfx','updatedocall','makevel','sucommand','sumean','suspeck1k2','updatehead','maxdiff','suconv','sumedian','suspike','upfort','maxints','sucountkey','sumigfd','susplit','usernames','merge2','sucvs4fowler','sumigffd','sustack','utmconv','merge2v','sucwt','sumiggbzo','sustatic','merge4','sudatumfd','sumiggbzoan','sustaticB','vel2stiff','mkparfile','sudatumk2dr','sumigprefd','sustaticrrs','velconv','mrafxzwt','sudatumk2ds','sumigpreffd','sustkvel','velpert','newcase','sudgwaveform','sumigprepspi','sustolt','velpertan','normray','sudiff','sumigpresp','sustrip','verhulst','overwrite','sudipdivcor','sumigps','susum','viewer3','pause','sudipfilt','sumigpspi','suswapbytes','vplusz','pdfhistogram','sudivcor','sumigpsti','susyncz','vtlvz','percent','sudivstack','sumigsplit','susynlv','vzest','precedence','sudmofk','sumigtk','susynlvcw','weekday','prplot','sudmofkcw','sumigtopo2d','susynlvfti','psbbox','sudmotivz','sumix','susynvxz','pscontour','sudmotx','sumixgathers','susynvxzcs','wpc1comp2','pscube','sudmovz','sumute','sutaper','wpc1uncomp2','pscubecontour','sudoc','suname','sutaup','wpccompress','psepsi','sudumptrace','sunan','sutaupnmo','wpcuncompress','psgraph','suea2df','sunhmospike','sutetraray','wptcomp','psimage','suedit','sunmo','sutifowler','wptuncomp','pslabel','sueipofi','sunmo_a','sutihaledmo','wtcomp','psmanager','suenv','sunormalize','sutivel','wtuncomp','psmerge','sufbpickw','sunull','sutrcount','xgraph','psmovie','sufctanismod','suocext','sutsq','ximage','pstopdfcymk','sufdmod1','suoldtonew','suttoz','xwigb','pswigb','sufdmod2','suop','sutvband','xy2z','pswigp','sufdmod2_pml','suop2','sutxtaper','z2xyz','randvel3d','sufft','supack1','suunpack1','zap','raydata','sufilter','supack2','suunpack2','rayt2d','sufind','supad','suutm','rayt2dan','sufind2','supaste','suvcat','rcpall','suflip','supef','suvel2df')  
        
            choices=[]
        
            new_lista=[]
       
            word=str(self.comando3.GetValue())
           
            print word
            
         
            for i in range(len(lista)):
                
                if word in (lista[i]):
                
                    print('---------------')
                    print(lista[i])
                    new_lista.append(lista[i])
                   
            choices=new_lista
          
                
            self.comando3 = wx.ComboBox(self.panel,6,'',(100,215),(150,-1),style=wx.CB_SORT, choices=choices)
            
            self.comando3.Bind(wx.EVT_KEY_DOWN, self.onkeypress3)  
            
                
        e.Skip()
        
         
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
  
########################################################################
class MainFrame(wx.Frame):
    """"""    
    #----------------------------------------------------------------------
    def __init__(self):
                
        dlg = WindowClass()
     
        dlg.ShowModal()
    def dwacad(self, event):
   
        self.frame2.Show()
        
        event.Skip()   
            
    def OnExit(self,e):
        self.Close(True)  
 
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()
#
class MainFrame2(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
          
            
        menuBar.Append(fileMenu, '&Cadastro') 
        
        menuBar.Append(editMenu, '&Consulta')
        
        self.SetMenuBar(menuBar) 
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        
        pub.subscribe(self.myListener, "frameListener2")
 
      
        dlg = WindowClass()
     
        dlg.ShowModal()
    
    def OnExit(self,e):
        self.Close(True)  
 
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()

#####################

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
    
##################        

