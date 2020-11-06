# Big Data Demo

Demo of 'Big Data' foundation of all North American Top of Book data

- Features :
   - 10-15 million msg/sec at open and close
   - Record all data on 1 Linux box
   - 3.0 TB on a reasonably big day - 2020 Election
   - 4.0 TB on a huge day : Market Drop > 1000 points
   - Recorder -> ReplaySvr -> Ticker Plant

- Recorder:
   - Multicast in via SolarFlare ef_vi API (Kernel-bypass)
   - 6 to 10 cores isolated to read in multicast; Real-time priority; Spinning
   - Packets dispatched to in-memory queues to tape
   - 1 thread per channel tape (CTA-A, UTP, OPRA1, COMEX, NYMEX)
   - Written to SSD

- ReplaySvr
   - Reads from Tape; Feeds 1 or more Ticker Plants
   - Regularly fans out 6 to 8 ticker plants, including OPRA
   - Sequenced data stream
   - May be configured to delay data

- Ticker Plant:
   - Last Value Cache of all North American Equities, Options, Futures, Indices
   - Each incoming channel runs in own thread
   - Sequenced data stream allows rewind from any time of day
   - Full rewind : 1-1.5 million msg/sec/thread
   - Can rewind 20 million msg/sec
