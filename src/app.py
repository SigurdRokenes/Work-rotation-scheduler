import config.config as cfg
import models.Shifts
import models.Worker
import simulators.Simulator


def main():
    #generate a list of names a, b, c ... z up to a number N
    
    print(cfg.N_WORKERS)
    names = [chr(i) for i in range(97, 97+cfg.N_WORKERS)]
    
    workers = [models.Worker.Worker(name, 100) for name in names]
    
    dayShift = models.Shifts.Shifts("Day", 8, 16)
    nightShift = models.Shifts.Shifts("Night", 16, 24)
    morningShift = models.Shifts.Shifts("Morning", 0, 8)
    shifts = [dayShift, nightShift, morningShift]
    
    simulators.Simulator.Simulator(shifts, workers)
    
    
    print(workers)



if __name__ == "__main__":
    main()
    