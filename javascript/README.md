simple webstorage api sessionstorage timer used for feedback latter request; project has a constraint of not relying on django session state document.ready calls start every load it'll go grab the current timer state and start it if it exists or do nothing if it does not, if you want to initialize the timer call reset, and we had a requirement of pausing it while a certain bootstrap modal is up so there is a pause functionality.
