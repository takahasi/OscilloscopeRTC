#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file OscilloscopeRTC.py
 @brief plotter RTC seems like oscilloscope
 @date $Date$


"""

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import numpy as np
import matplotlib.pyplot as plt

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
oscilloscopertc_spec = ["implementation_id", "OscilloscopeRTC", 
		 "type_name",         "OscilloscopeRTC", 
		 "description",       "plotter RTC seems like oscilloscope", 
		 "version",           "1.0.0", 
		 "vendor",            "takahasi", 
		 "category",          "debu", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

xdata = np.zeros(100)
xdata = np.zeros(100)
float_data = np.zeros(100)
double_data = np.zeros(100)
short_data = np.zeros(100)
long_data = np.zeros(100)
time = 0
lines = 0


##
# @class OscilloscopeRTC
# @brief plotter RTC seems like oscilloscope
# 
# 
class OscilloscopeRTC(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_bool = RTC.TimedBoolean(RTC.Time(0,0),0)
		"""
		"""
		self._boolIn = OpenRTM_aist.InPort("bool", self._d_bool)
		self._d_boolSeq = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
		"""
		"""
		self._boolSeqIn = OpenRTM_aist.InPort("boolSeq", self._d_boolSeq)
		self._d_char = RTC.TimedChar(RTC.Time(0,0),0)
		"""
		"""
		self._charIn = OpenRTM_aist.InPort("char", self._d_char)
		self._d_charSeq = RTC.TimedCharSeq(RTC.Time(0,0),[])
		"""
		"""
		self._charSeqIn = OpenRTM_aist.InPort("charSeq", self._d_charSeq)
		self._d_double = RTC.TimedDouble(RTC.Time(0,0),0)
		"""
		"""
		self._doubleIn = OpenRTM_aist.InPort("double", self._d_double)
		self._d_doubleSeq = RTC.TimedDouble(RTC.Time(0,0),0)
		"""
		"""
		self._doubleSeqIn = OpenRTM_aist.InPort("doubleSeq", self._d_doubleSeq)
		self._d_float = RTC.TimedFloat(RTC.Time(0,0),0)
		"""
		"""
		self._floatIn = OpenRTM_aist.InPort("float", self._d_float)
		self._d_floatSeq = RTC.TimedFloatSeq(RTC.Time(0,0),[])
		"""
		"""
		self._floatSeqIn = OpenRTM_aist.InPort("floatSeq", self._d_floatSeq)
		self._d_long = RTC.TimedLong(RTC.Time(0,0),0)
		"""
		"""
		self._longIn = OpenRTM_aist.InPort("long", self._d_long)
		self._d_longSeq = RTC.TimedLongSeq(RTC.Time(0,0),[])
		"""
		"""
		self._longSeqIn = OpenRTM_aist.InPort("longSeq", self._d_longSeq)
		self._d_octet = RTC.TimedOctet(RTC.Time(0,0),0)
		"""
		"""
		self._octetIn = OpenRTM_aist.InPort("octet", self._d_octet)
		self._d_octetSeq = RTC.TimedOctetSeq(RTC.Time(0,0),[])
		"""
		"""
		self._octetSeqIn = OpenRTM_aist.InPort("octetSeq", self._d_octetSeq)
		self._d_short = RTC.TimedShort(RTC.Time(0,0),0)
		"""
		"""
		self._shortIn = OpenRTM_aist.InPort("short", self._d_short)
		self._d_shortSeq = RTC.TimedShortSeq(RTC.Time(0,0),[])
		"""
		"""
		self._shortSeqIn = OpenRTM_aist.InPort("shortSeq", self._d_shortSeq)
		self._d_velocity2d = RTC.TimedVelocity2D(RTC.Time(0,0),0)
		"""
		"""
		self._velocity2dIn = OpenRTM_aist.InPort("velocity2d", self._d_velocity2d)
		self._d_velocity3d = RTC.TimedVelocity3D(RTC.Time(0,0),0)
		"""
		"""
		self._velocity3dIn = OpenRTM_aist.InPort("velocity3d", self._d_velocity3d)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("bool",self._boolIn)
		self.addInPort("boolSeq",self._boolSeqIn)
		self.addInPort("char",self._charIn)
		self.addInPort("charSeq",self._charSeqIn)
		self.addInPort("double",self._doubleIn)
		self.addInPort("doubleSeq",self._doubleSeqIn)
		self.addInPort("float",self._floatIn)
		self.addInPort("floatSeq",self._floatSeqIn)
		self.addInPort("long",self._longIn)
		self.addInPort("longSeq",self._longSeqIn)
		self.addInPort("octet",self._octetIn)
		self.addInPort("octetSeq",self._octetSeqIn)
		self.addInPort("short",self._shortIn)
		self.addInPort("shortSeq",self._shortSeqIn)
		self.addInPort("velocity2d",self._velocity2dIn)
		self.addInPort("velocity3d",self._velocity3dIn)
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
		global time, lines, xdata
		global float_data, double_data, short_data, long_data

		xdata = np.zeros(100)
		float_data = np.zeros(100)
		double_data = np.zeros(100)
		short_data = np.zeros(100)
		long_data = np.zeros(100)

		plt.figure()
		plt.legend(loc='upper left')
		lines, = plt.plot(xdata, float_data)
		time = 0
		plt.ylim(0, 5)
		plt.xlabel("time")
		plt.ylabel("value")

		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
		plt.close()
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
		global time, lines, xdata
		global float_data, double_data, short_data, y_float_data, long_data

		is_plot = False
		time += 0.001
		
		if self._floatIn.isNew():
			data = self._floatIn.read()
			float_data = np.append(float_data, data.data)
			float_data = np.delete(float_data, 0)
			is_plot = True

		if self._doubleIn.isNew():
			data = self._doubleIn.read()
			double_data = np.append(double_data, data.data)
			double_data = np.delete(double_data, 0)
			is_plot = True

		if is_plot:
			xdata = np.append(xdata, time)
			xdata = np.delete(xdata, 0)
			lines.set_xdata(xdata)
			lines.set_ydata(float_data)
			plt.xlim(min(xdata) * 1.1, max(xdata) * 1.1)
			plt.ylim(min(float_data) * 1.1, max(float_data) * 1.1)
			plt.plot(xdata, float_data, color="blue", linewidth=1.0, linestyle="-", label="float")

			lines.set_ydata(double_data)
			plt.xlim(min(xdata) * 1.1, max(xdata) * 1.1)
			plt.ylim(min(double_data) * 1.1, max(float_data) * 1.1)
			plt.plot(xdata, double_data, color="red", linewidth=1.0, linestyle="-", label="double")
			plt.pause(.01)

		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def OscilloscopeRTCInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=oscilloscopertc_spec)
    manager.registerFactory(profile,
                            OscilloscopeRTC,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    OscilloscopeRTCInit(manager)

    # Create a component
    comp = manager.createComponent("OscilloscopeRTC")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

