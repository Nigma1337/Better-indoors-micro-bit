let air = 0
basic.forever(function () {
    while (true) {
        basic.showString("Temp: ")
        basic.showNumber(input.temperature())
        basic.showString("air: ")
        air = pins.analogReadPin(AnalogPin.P3)
        if (air > 900) {
            basic.showString("Bad")
        }
        else if (air > 600) {
            basic.showString("Decent")
        }
        else {
            basic.showString("Good")
        }
    }
})
