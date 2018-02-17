# docimages_cut_n_pastes.py
# Sends commands to get images for the manual.
# Images for cut_n_paste manipulation.

# Make sure Audacity is running first and that mod-script-pipe is enabled
# before running this script.

#load and run the common core.
exec( open("docimages_core.py" ).read() )

def gappyTrack() :
    loadMonoTracks(1)
    # A mono track
    do( 'Select: Start=0 End=10')
    do( 'SplitCut' )
    do( 'Select: Start=60 End=100')
    do( 'SplitCut' )
    do( 'Select: Start=30 End=50')

def cut_n_paste_imagesA() :
    # Split and move
    gappyTrack()
    capture( 'CutAndPaste001.png', 'All_Tracks' )
    do( 'Split' )
    capture( 'CutAndPaste002.png', 'All_Tracks' )
    do( 'SetClip: At=55 Start=60')
    capture( 'CutAndPaste003.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste004.png', 'All_Tracks' )

def cut_n_paste_imagesB() :
    # SplitNew
    gappyTrack()
    capture( 'CutAndPaste005.png', 'All_Tracks' )
    do( 'SplitNew' )
    capture( 'CutAndPaste006.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste007.png', 'All_Tracks' )

def cut_n_paste_imagesC() :
    # Join
    gappyTrack()
    do( 'Select: Start=45 End=75')
    do( 'Split' )
    do( 'Select: Start=39 End=129')
    capture( 'CutAndPaste008.png', 'All_Tracks' )
    do( 'Join' )
    capture( 'CutAndPaste009.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste010.png', 'All_Tracks' )
    # Detach at silences
    do( 'Select: Start=0 End=150')
    do( 'Join' )
    capture( 'CutAndPaste011.png', 'All_Tracks' )
    do( 'Select: Start=0 End=150')
    do( 'Disjoin' )
    capture( 'CutAndPaste012.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste013.png', 'All_Tracks' )

def cut_n_paste_imagesD() :
    #Copy and Paste
    gappyTrack()
    do( 'Select: Start=15 End=20')
    do( 'Copy' )
    capture( 'CutAndPaste014.png', 'All_Tracks' )
    #Pasting into
    do( 'Select: Start=45 End=45')
    capture( 'CutAndPaste015.png', 'All_Tracks' )
    do( 'Paste' )
    capture( 'CutAndPaste016.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste017.png', 'All_Tracks' )

    gappyTrack()
    do( 'Select: Start=15 End=20')
    do( 'Copy' )
    #Pasting before
    do( 'Select: Start=5 End=5')
    capture( 'CutAndPaste018.png', 'All_Tracks' )
    do( 'Paste' )
    capture( 'CutAndPaste019.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste030.png', 'All_Tracks' )

    #pasting before with no movement (cheat)
    do( 'Select: Start=11 End=16')
    do( 'Cut' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste031.png', 'All_Tracks' )
    do( 'Select: Start=5 End=10')
    capture( 'CutAndPaste032.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    
def cut_n_paste_imagesE() :    
    # Duplicate
    gappyTrack()
    capture( 'CutAndPaste033.png', 'All_Tracks' )
    do( 'Duplicate' )
    capture( 'CutAndPaste034.png', 'All_Tracks' )
    do( 'Select: Start=0 End=0')
    capture( 'CutAndPaste035.png', 'All_Tracks' )
    

cut_n_paste_imagesA()
cut_n_paste_imagesB()
cut_n_paste_imagesC()
cut_n_paste_imagesD()
cut_n_paste_imagesE()
