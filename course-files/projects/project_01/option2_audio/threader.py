import threading
import psonic


class SonicPiSample(object):
    def __init__(self, manager, sample):
        self.manager = manager
        self.sample = sample

    def start(self):
        threading.Thread(
            target=self.__start_sample
        ).start()

    def __start_sample(self):
        with self.manager.condition:
            self.manager.condition.wait() # wait for message
        self.sample(tempo=self.manager.tempo)


class SonicPiLoop(object):
    def __init__(self, manager, sample):
        self.stop_event = None
        self.manager = manager
        self.sample = sample
    
    def __start_loop(self):
        while not self.stop_event.is_set():
            with self.manager.condition:
                self.manager.condition.wait() # wait for message
            # print('playing...')
            self.sample(tempo=self.manager.tempo)

    def is_running(self):
        return self.stop_event and not self.stop_event.is_set()

    def stop(self):
        if self.is_running():
            self.stop_event.set()
    
    def start(self):
        self.stop_event = threading.Event()
        threading.Thread(
            target=self.__start_loop
        ).start()


class SonicPiController(object):
    def __init__(self, tempo=1, riff=None):
        self.tempo = tempo
        self.riff = riff
        self.condition = threading.Condition()
        self.stop_event = threading.Event()
        threading.Thread(
            target=self.start_controller
        ).start()

    def start_controller(self):
        while not self.stop_event.is_set():
            with self.condition:
                # print('notify..')
                self.condition.notifyAll() # notify
            if self.riff:
                self.riff(tempo=self.tempo)
            else:
                self.default_riff(tempo=self.tempo)
               
    def default_riff(self, tempo):
        psonic.sample(psonic.DRUM_BASS_SOFT, amp=0.5)
        psonic.sleep(1 * tempo)

    def is_running(self):
        return self.stop_event and not self.stop_event.is_set()

    def stop(self):
        if self.is_running():
            print('controller stopped')
            self.stop_event.set()