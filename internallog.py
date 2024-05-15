from enum import Enum

class LogLevel(Enum):
	NaN = 0
	Error = 1
	Warning = 2
	Trace = 3
	Debug = 4
	Info = 5

	def __le__(self, other) -> bool:
		return self.value <= other.value

class InternalLog(object):
	
	def __init__(self, lv:LogLevel = LogLevel.NaN) -> None:
		self.__lv = lv

		self.__map_func = {}
		self.__install_log(lv)
		print (self.__map_func)

	def set_log_level(self, lv:LogLevel) -> None:
		self.__install_log(lv)
		self.__lv = lv

	def get_log_level(self) -> LogLevel:
		return self.__lv

	def __print(self, *values:object, sep : str = None, end : str = None) -> None:
		print(*values, sep = sep, end = end)

	def __dummy(self, *values:object, sep : str = None, end : str = None) -> None:
		pass

	def error(self, *values:object) -> None:
		log_out = self.__map_func[LogLevel.Error]
		log_out('[Error]', end='')
		log_out(*values)

	def warning(self, *values:object) -> None:
		log_out = self.__map_func[LogLevel.Warning]
		log_out('[Warning]', end='')
		log_out(*values)

	def trace(self, *values:object) -> None:
		log_out = self.__map_func[LogLevel.Trace]
		log_out('[Trace]', end='')
		log_out(*values)

	def debug(self, *values:object) -> None:
		log_out = self.__map_func[LogLevel.Debug]
		log_out('[Debug]', end='')
		log_out(*values)


	def info(self, *values:object) -> None:
		log_out = self.__map_func[LogLevel.Info]
		log_out('[Info]', end='')
		log_out(*values)

	def __install_log(self, lv:LogLevel) -> None:
		for i in LogLevel:
			if i <= lv:
				self.__map_func[i] = self.__print
			else:
				self.__map_func[i] = self.__dummy

