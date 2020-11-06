#!/usr/bin/python
#################################################################
#
#  DumpMon.py
#     Dump MonXxxx output, messages delinated ANSI_HOME 
#
#  REVISION HISTORY:
#      1 NOV 2020 jcs  Created.
#      5 NOV 2020 jcs  gzip
#
#  (c) 1994-2020, Gatea Ltd.
#################################################################
import gzip, sys, time

## Hard-coded : Normal

_ANSI_CLEAR     = '\x1b[H\x1b[m\x1b[J'
_ANSI_HOME      = '\x1b[1;1H\x1b[K'

## Hard-coded : top output

_ANSI_TOP_CLEAR = '\x1b[?1h\x1b=\x1b[H\x1b[J\x1b[m\x0f'
_ANSI_TOP_HOME  = 'top - '
_ANSI_TOP_SOM   = '\x1b[H'
_ANSI_TOP_SOL   = '\x1b[m\x0f\x1b[1m'
_ANSI_TOP_SOL1  = '\x1b[7m'
_ANSI_TOP_EOL   = '\x1b[m\x0f\x1b[K'
_ANSI_TOP_BOLD  = '\x1b[m\x0f'
_ANSI_TOP_CRLF  = '\x1b[K\x0a'
_ANSI_TOP_CRLF1 = _ANSI_TOP_CRLF + '\x1b[7m'


#############################
#                           #
#        main()             #
#                           #
#############################
if __name__ == '__main__':
   #
   # args : <mon.out> -u <rate> -s <SkipTo HH:MM:SS>
   #
   exe  = sys.argv[0]
   argc = len( sys.argv )
   help = [ 'Usage: %s <mon.out>' % exe,
            '-u <rate>',
            '-s <SkipTo HH:MM:SS>',
            '-o <Omit>',
            '-rows <MaxRows>',
            '-top <True|False>' ]
   if argc < 2:
      print ' '.join( help )
      sys.exit()
   sdb = []
   pf  = sys.argv[1]
   try:
      gz = pf.endswith( '.gz' )
      if gz: fp = gzip.open( pf, 'rb' )
      else:  fp = open( pf, 'rb' )
      if gz: print 'gunzip( %s ) ... ' % pf
      sdb = fp.readlines()
      fp.close()
   except:
      sdb = []
   ns = len( sdb )
   print _ANSI_CLEAR
   sz = 0
   for l in sdb:
      sz = max( len( l ), sz )
##   print '%d lines read; MaxLen = %d' % ( ns, sz )
   if not ns:
      print 'Nothing to do; Exitting ...'
      sys.exit()
   #
   # Rest of the args
   #
   rate = 1.0
   skip = None
   omit = []
   top  = False
   rows = 9999999
   for n in range( 2,argc,2 ):
      flag = sys.argv[n]
      val  = sys.argv[n+1]
      if flag == '-u':      rate = float( val )
      elif flag == '-s':    skip  = val
      elif flag == '-o':    omit += val.split(',')
      elif flag == '-top':  top   = ( val == 'True' )
      elif flag == '-rows': rows  = int( val )
      else:
         print 'Invalid flag %s' % flag
         print ' '.join( help )
         print 'Exitting ...'
         sys.exit()
   CLEAR = _ANSI_CLEAR
   HOME  = _ANSI_HOME
   SLOP  = []
   if top:
      CLEAR = _ANSI_TOP_CLEAR
      HOME  = _ANSI_TOP_HOME
      SLOP  = [ _ANSI_TOP_SOM ]
      SLOP += [ _ANSI_TOP_SOL,  _ANSI_TOP_SOL1 ]
      SLOP += [ _ANSI_TOP_EOL, _ANSI_TOP_BOLD ]
      SLOP += [ _ANSI_TOP_CRLF, _ANSI_TOP_CRLF1 ]
   #
   # Rock on ...
   #
   pg  = []
   if skip:
      print 'SKIP-ing to %s' % skip
   try:
      #
      # Start of Data
      #
      for j in range( ns ):
         l = sdb[j]
         if skip:
            if l.count( CLEAR ) or l.count( HOME ):
               if top:
                  ll = l.split( HOME )[1]
                  t0 = ll.split()[0]
               else:
                  t0 = l.replace( '\n','' ).split()[1]
               if t0 >= skip:
                  ss  = 'SKIP to %s : %d lines skipped' % ( t0, j )
                  ss += '; <ENTER> to continue'
                  raw_input( ss )
                  break ## for-j
         elif l.count( CLEAR ):
            break ## for-j
      #
      # Rock on
      #
      for i in range( j, ns ):
         l = sdb[i]
         if l.count( HOME ) and len( pg ):
            print ''.join( pg[:rows] )
            pg = []
            time.sleep( rate )
         bOK = True 
         for o in omit:
            bOK &= not l.count( o )
         if bOK:
            for slop in SLOP:
               l = l.replace( slop, '' )
            if top and not len( pg ):
               l = _ANSI_HOME + _ANSI_TOP_HOME + l.split( _ANSI_TOP_HOME )[1]
            pg += [ l ]
   except KeyboardInterrupt:
      pass
   print ''.join( pg[:rows] )
