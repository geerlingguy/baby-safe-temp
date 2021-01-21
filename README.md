# Baby Safe Temperature Monitor

![Lint](https://github.com/geerlingguy/baby-safe-temp/workflows/Lint/badge.svg?event=push)

This project is meant to build a temperature safety monitor for a baby or small child's room.

Studies have shown the risk for Sudden Infant Death Syndrome (SIDS) increases when a baby's room temperature is outside the range of 20-22.2°C (68-72°F).

This little bit of MicroPython code works with the Raspberry Pi RP2040 chip in the [Raspberry Pi Pico](https://pico.raspberrypi.org) microcontroller to monitor the temperature in a room, and show whether the temperature is safe via three status LEDs:

  - Green means safe for baby
  - Red means too hot
  - Blue means too cold

Obviously, this is NOT a medical device, just a little side project from a crazy guy who once built a [cluster of Pis to monitor his house's room temperatures](https://github.com/geerlingguy/temperature-monitor).

If you want to see how it was put together and used, please check out my [Review of the Raspberry Pi Pico microcontroller](TODO: Link) on [my YouTube channel](https://www.youtube.com/c/JeffGeerling).

## Circuit Diagram

<p align="center"><img src="images/baby-temp-mon-sketch.png?raw=true" width="600" height="auto" alt="Fritzing sketch of LED connections to Raspberry Pi Pico" /></a></p>

See also: [Fritzing sketch](images/baby-temp-mon-sketch.fzz)

## Usage

  1. Make sure you have MicroPython flashed to your Raspberry Pi Pico.
  2. Copy the `main.py` script from this repository to your board.
  3. Connect LEDs to the board following the circuit diagram shown above.
  4. Power up the board, and watch the LEDs.

## Similar Projects

I also created a Raspberry Pi-based temperature monitoring cluster for my entire house back in 2016, and I open sourced the design and code for that system.

You can find it here: [Raspberry Pi Temperature Monitoring App](https://github.com/geerlingguy/temperature-monitor).

## License

MIT License

## Author

This project was created by [Jeff Geerling](https://www.jeffgeerling.com) in 2021.
