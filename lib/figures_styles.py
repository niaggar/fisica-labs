import matplotlib.pyplot as plt

font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'black','size':15}
font3 = {'family':'serif','color':'black','size':15}
font4 = {'family':'serif','color':'black','size':15}


class CreateFigure:
    fig = None

    def p_create(self, height, widht):
        '''Crea una figura con las dimensiones dadas'''
        self.fig = plt.figure()
        self.fig.set_figheight(height)
        self.fig.set_figwidth(widht)

    def p_add_text(self, text, x, y):
        '''Agrega texto a la figura'''
        plt.text(x, y, text, fontdict = font4)

    def p_xlabel(self, label):
        '''Agrega un label al eje x'''
        plt.xlabel(label, fontdict = font2)

    def p_ylabel(self, label):
        '''Agrega un label al eje y'''
        plt.ylabel(label, fontdict = font2)

    def p_title(self, title):
        '''Agrega un titulo a la figura'''
        plt.title(title, fontdict = font1)

    def p_legend(self):
        '''Agrega leyendas a la figura'''
        self.legend = plt.legend(loc='upper right')
        for text in self.legend.texts:
            text.set_fontsize(font3['size'])
            text.set_family(font3['family'])

    def p_plot(self, x, y, color, label = None, format = None):
        '''Agrega una linea a la figura'''
        if format == None:
            plt.plot(x, y, color = color, label = label)
        else:
            plt.plot(x, y, format, color = color, label = label)

    def p_scatter(self, x, y, color, label = None):
        '''Agrega un scatter a la figura'''
        plt.scatter(x, y, color = color, label = label)

    def p_fill_between(self, x, y1, y2, color, alpha = 0.2):
        '''Agrega un fill_between a la figura'''
        plt.fill_between(x, y1, y2, color = color, alpha = alpha)

    def p_show(self):
        '''Muestra la figura'''
        plt.show()
