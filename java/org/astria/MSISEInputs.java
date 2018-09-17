/*
 * MSISEInputs.java - Class for reading MSISE space weather data.
 * Copyright (C) 2018 Shiva Iyer <shiva.iyer AT utexas DOT edu>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

package org.astria;

import java.util.Hashtable;
import org.orekit.forces.drag.atmosphere.NRLMSISE00InputParameters;
import org.orekit.time.AbsoluteDate;

public class MSISEInputs implements NRLMSISE00InputParameters
{
    protected AbsoluteDate mindate;
    protected AbsoluteDate maxdate;
    protected Hashtable swdata;
    
    public MSISEInputs(AbsoluteDate min, AbsoluteDate max, Hashtable sw)
    {
	this.mindate = min;
	this.maxdate = max;
	this.swdata = sw;
    }

    public AbsoluteDate getMinDate()
    {
	return(mindate);
    }

    public AbsoluteDate getMaxDate()
    {
	return(maxdate);
    }

    public double getDailyFlux(AbsoluteDate date)
    {
	String p = new AbsoluteDate(date, -86400.0).toString();
	String k = p.substring(0, 4) + p.substring(5, 7) + p.substring(8, 10);
	float[] v = (float[]) swdata.get(k);
	return(v[26]);
    }

    public double getAverageFlux(AbsoluteDate date)
    {
	String p = date.toString();
	String k = p.substring(0, 4) + p.substring(5, 7) + p.substring(8, 10);
	float[] v = (float[]) swdata.get(k);
	return(v[28]);
    }

    public double[] getAp(AbsoluteDate date)
    {
	double[] ap = new double[7];
	for (int i = 0; i <= 6; i++)
	{
	    if (i == 0)
	    {
		String p = date.toString();
		String k = p.substring(0, 4) + p.substring(5, 7) + p.substring(8, 10);
		float[] v = (float[]) swdata.get(k);
		ap[0] = v[22];
	    }
	    else if (i <= 4)
	    {
		String p = (new AbsoluteDate(date, -10800.0*(i - 1))).toString();
		String k = p.substring(0, 4) + p.substring(5, 7) + p.substring(8, 10);
		float[] v = (float[]) swdata.get(k);
		ap[i] = v[Integer.parseInt(p.substring(11, 13)) % 3 + 14];
	    }
	    else
	    {
		for (int j = 8*i - 36; j <= 8*i - 29; j++)
		{
		    String p = (new AbsoluteDate(date, -10800.0*(j - 1))).toString();
		    String k = p.substring(0, 4) + p.substring(5, 7) + p.substring(8, 10);
		    float[] v = (float[]) swdata.get(k);
		    ap[i] += v[Integer.parseInt(p.substring(11, 13)) % 3 + 14];
		}
		ap[i] = ap[i]/8;
	    }
	}

	return(ap);
    }
}
