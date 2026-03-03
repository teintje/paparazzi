


#include "firmwares/rotorcraft/navigation.h"

void my_custom_yaw_control(void)
{
    nav.setpoint_mode = NAV_SETPOINT_MODE_ATTITUDE;
    nav_set_heading_deg(3.141f);
}