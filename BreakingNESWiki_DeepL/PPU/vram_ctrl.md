# VRAM Controller

![ppu_locator_vram_ctrl](/BreakingNESWiki/imgstore/ppu/ppu_locator_vram_ctrl.jpg)

The circuitry is the "auxiliary brain" of the bottom of the PPU to control the VRAM interface.

In addition, the controller also includes a READ BUFFER (RB), an intermediate data storage for exchange with VRAM.

## Transistor Circuit

<img src="/BreakingNESWiki/imgstore/ppu/vram_control_tran.jpg" width="1000px">

Anatomically the circuit is divided into 2 large halves, the left one is more connected to the `WR` control signal and the right one to the `RD`.
Each half includes an RS trigger and a delay line that automatically sets the trigger.

The circuit outputs a number of control lines to the outside:
- RD: to /RD output
- WR: to /WR output
- /ALE: to the ALE output (ALE=1 when the AD bus works as an address bus, ALE=0 when AD works as a data bus)
- TSTEP: to the DATAREAD circuit, allows TV/TH counters to perform incremental
- DB/PAR: on the DATAREAD circuit, connects the internal PPU DB bus to the PAR (PPU address register) pseudo register
- PD/RB: connects the external PPU bus to a read buffer to load a new value into it
- TH/MUX: send the TH counter to the MUX input, causing this value to go into the palette as an index.
- XRB: enable tri-state logic that disconnects the PPU read buffer from the internal data bus.

## Logic

<img src="/BreakingNESWiki/imgstore/ppu/vram_control_logisim.jpg" width="1000px">

To say something more specific, you need to first examine the rest of the PPU parts.

TBD.

## Read Buffer (RB)

Located to the right of [OAM FIFO](fifo.md).

![ppu_readbuffer](/BreakingNESWiki/imgstore/ppu/ppu_readbuffer.jpg)

![ppu_logisim_rb](/BreakingNESWiki/imgstore/ppu/ppu_logisim_rb.jpg)
