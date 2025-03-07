# utilities.py - Various utilities.
# Copyright (C) 2020-2021 University of Texas
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import List
from orbdetpy.rpc.messages_pb2 import DoubleArray, InterpolateEphemerisInput, TransformFrameInput
from orbdetpy.rpc.server import RemoteServer
from orbdetpy.rpc.utilities_pb2_grpc import UtilitiesStub

def interpolate_ephemeris(source_frame: int, times: List[float], states, num_points: int,
                          dest_frame: int, interp_start: float, interp_end: float, step_size: float):
    """Interpolate the given state vectors.

    Parameters
    ----------
    source_frame : Source reference frame; a constant from Frame.
    times : Times of state vectors; each a TT offset from J2000 epoch [s].
    states : State vectors to interpolate.
    num_points : Number of states to use for interpolation.
    dest_frame : Destination reference frame; a constant from Frame.
    interp_start : Interpolation start time.
    interp_end : Interpolation end time.
    step_size : Interpolation step size [s].

    Returns
    -------
    Interpolated times and state vectors.
    """

    resp = _utilities_stub.interpolateEphemeris(InterpolateEphemerisInput(
        source_frame=source_frame, time=times, ephem=[DoubleArray(array=s) for s in states], num_points=num_points,
        dest_frame=dest_frame, interp_start=interp_start, interp_end=interp_end, step_size=step_size))
    return(resp.array)

def get_density(drag_model: int, time: float, lla: List[float])->List[float]:
    """Calculate atmospheric neutral density.

    Parameters
    ----------
    drag_model : Atmospheric drag model; a constant from DragModel.
    time : Offset in TT from J2000 epoch [s]. Give a list for bulk calculations.
    lla : WGS-84 latitude, longitude, altitude. Give a list of lists for bulk calculations.

    Returns
    -------
    Atmospheric neutral density [kg/m^3] at the specified coordinates.
    """

    if (isinstance(time, float) or isinstance(time, str)):
        time, lla = [time], [lla]
    if (isinstance(time[0], float)):
        resp = _utilities_stub.getDensity(TransformFrameInput(
            time=time, pva=[DoubleArray(array=x) for x in lla], dest_frame=str(drag_model)))
    else:
        resp = _utilities_stub.getDensity(TransformFrameInput(
            UTC_time=time, pva=[DoubleArray(array=x) for x in lla], dest_frame=str(drag_model)))
    return(resp.array)

if (__name__ != '__main__'):
    __pdoc__ = {m: False for m in ("DoubleArray", "InterpolateEphemerisInput")}
    _utilities_stub = UtilitiesStub(RemoteServer.channel())
