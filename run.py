def main():
    def submit():
        sphere_fct = lambda x: sum([x[i]**2 for i in range(len(x))])
        rosenbrock_fct = lambda x: sum([100*(x[i+1]-x[i])**2+(1-x[i])**2 for i in range(len(x)-1)]) if len(x)>1 else np.nan
        rastrigin_fct = lambda x: 10*len(x)+sum([x[i]**2-10*np.cos(2*np.pi*x[i]) for i in range(len(x))])
        qing_fct = lambda x: sum([(x[i]**2-i-1)**2 for i in range(len(x))])

        objective = objectiveEntry.get()
        objective_fct = rosenbrock_fct

        n, d = int(popEntry.get()), int(dimensionEntry.get())
        range_min, range_max = (int(minRangeFrom.get()), int(minRangeTo.get())), (int(maxRangeFrom.get()), int(maxRangeTo.get()))

        T = int(iterEntry.get())

        from metaheuristics.firefly import FireflyAlgorithm

        a, b, g = float(alphaEntry.get()), float(betaEntry.get()), float(gammaEntry.get())

        firefly = FireflyAlgorithm(d=d, n=n, range_min=range_min, range_max=range_max,
                           alpha=a, beta_max=b, gamma=g)

        from matplotlib.pyplot import ion, show
        import webbrowser
        import os
        for algo in [firefly]:
            solution, latency = algo.search(objective, objective_fct, T, visualize=True)
            temp = algo
            algo.generate_gif()
            webbrowser.open('file://'+os.getcwd()+'/firefly.gif')

        temp.plot_history()

        
        
        

    def reset():
        import os, shutil
        folder = os.getcwd()+'/images/firefly/'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Canvas, mainloop, PhotoImage, Spinbox
    master = Tk()

    master.geometry('270x350')
    master.title('Firefly Algorithm Visualization')

    filename = PhotoImage(file = "icons/firefly.png")
    background_label = Label(master, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    masterFull = Canvas(master,
                        height = '350',
                        width = '270')
    masterFull.pack()

    masterFull.create_image(135, 175,
                            image = filename)
                     
    masterFull.create_text(95, 25,
                           text = 'Objective:',
                           font = 'calibri 12')
    objectiveEntry = Spinbox(master,
                           bd = '2', values = ('min', 'max'))
    masterFull.create_window(200, 25,
                             window = objectiveEntry)
    
    masterFull.create_text(90, 75,
                           text = 'Dimension:',
                           font = 'calibri 12')
    dimensionEntry = Entry(master,
                           bd = '2')
    dimensionEntry.insert(0, '2')
    masterFull.create_window(200, 75,
                             window = dimensionEntry)
    
    masterFull.create_text(76, 100,
                           text = 'Population Size:',
                           font = 'calibri 12')
    popEntry = Entry(master,
                           bd = '2')
    popEntry.insert(0, '10')
    masterFull.create_window(200, 100,
                             window = popEntry)
    
    masterFull.create_text(90, 125,
                           text = 'Min Range:',
                           font = 'calibri 12')
    masterFull.create_text(200, 125,
                           text = 'to',
                           font = 'calibri 12')
    minRangeFrom = Entry(master,
                        bd = '2',
                        width = '5')
    minRangeFrom.insert(0, '-5')
    minRangeTo = Entry(master,
                      bd = '2',
                      width = '5')
    minRangeTo.insert(0, '-5')
    masterFull.create_window(170, 125,
                             window = minRangeFrom)
    masterFull.create_window(230, 125,
                             window = minRangeTo)
    
    masterFull.create_text(89, 150,
                           text = 'Max Range:',
                           font = 'calibri 12')
    masterFull.create_text(200, 150,
                           text = 'to',
                           font = 'calibri 12')
    maxRangeFrom = Entry(master,
                        bd = '2',
                        width = '5')
    maxRangeFrom.insert(0, '5')
    maxRangeTo = Entry(master,
                      bd = '2',
                      width = '5')
    maxRangeTo.insert(0, '5')
    masterFull.create_window(170, 150,
                             window = maxRangeFrom)
    masterFull.create_window(230, 150,
                             window = maxRangeTo)
    
    masterFull.create_text(94, 175,
                           text = 'Iterations:',
                           font = 'calibri 12')
    iterEntry = Entry(master,
                           bd = '2')
    iterEntry.insert(0, '50')
    masterFull.create_window(200, 175,
                             window = iterEntry)
    
    masterFull.create_text(107, 200,
                           text = 'Alpha:',
                           font = 'calibri 12')
    alphaEntry = Entry(master,
                           bd = '2')
    alphaEntry.insert(0, '0.5')
    masterFull.create_window(200, 200,
                             window = alphaEntry)
    
    masterFull.create_text(109, 225,
                           text = 'Beta:',
                           font = 'calibri 12')
    betaEntry = Entry(master,
                           bd = '2')
    betaEntry.insert(0, '1.0')
    masterFull.create_window(200, 225,
                             window = betaEntry)
    
    masterFull.create_text(99, 250,
                           text = 'Gamma:',
                           font = 'calibri 12')
    gammaEntry = Entry(master,
                           bd = '2')
    gammaEntry.insert(0, '0.5')
    masterFull.create_window(200, 250,
                             window = gammaEntry)

    submitBtn = Button(master,
                       text = 'Submit',
                       bd = '1',
                       command = submit,
                       font = 'calibri 12')
    masterFull.create_window(200, 300,
                             window = submitBtn)

    resetBtn = Button(master,
                       text = 'Clear',
                       bd = '1',
                       command = reset,
                       font = 'calibri 12')
    masterFull.create_window(100, 300,
                             window = resetBtn)
    mainloop()

if __name__ == "__main__":
    main()
