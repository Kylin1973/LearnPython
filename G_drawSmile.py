#!/usr/bin/python
# -*- coding: utf-8 -*-
#python 2.7.10
#copyRight by kylin
import wx

class Smiley(wx.PyControl):
    def __init__(self, parent, size = (100,100)):
        super(Smiley, self).__init__(parent, size = size, style = wx.NO_BORDER)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        """Draw the image on to the panel"""
        dc = wx.PaintDC(self)
        rect = self.GetClientRect()
        dc.SetPen(wx.BLACK_PEN)
        yellowbrush = wx.Brush(wx.Colour(255, 255, 0))
        dc.SetBrush(yellowbrush)

        cx = (rect.width/2)+rect.x
        cy = (rect.width/2)+rect.y
        radius = min(rect.width, rect.height)/2
        dc.DrawCircle(cx, cy, radius)
        eyesz = (rect.width/8, rect.height/8)
        eyepos = (cx/2, cy/2)
        dc.SetBrush(wx.BLUE_BRUSH)
        dc.DrawRectangle(eyepos[0], eyepos[1], eyesz[0], eyesz[1])
        eyepos = (eyepos[0]+(cx-eyesz[0]),eyepos[1])
        dc.DrawRectangle(eyepos[0], eyepos[1], eyesz[0], eyesz[1])
        dc.SetBrush(yellowbrush)
        startpos = (cx/2,(cy/2)+cy)
        endpos = (cx+startpos[0],startpos[1])
        dc.DrawArc(startpos[0], startpos[1], endpos[0], endpos[1], cx, cy)
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangle(startpos[0], cy, endpos[0]-startpos[0], startpos[1]-cy)

class MyFrame(wx.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MyFrame, self).__init__(parent, *args, **kwargs)
        self.parent = wx.Panel(self)
        Smiley(self.Panel)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="DrawSmile",size = [500,500])
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


if __name__ = "__main__":
    app = MyApp(False)
    app.MainLoop()
