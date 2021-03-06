class ITypeLibExporterNotifySink:
 """ Provides a callback mechanism for the assembly converter to inform the caller of the status of the conversion,and involve the caller in the conversion process itself. """
 def ReportEvent(self,eventKind,eventCode,eventMsg):
  """
  ReportEvent(self: ITypeLibExporterNotifySink,eventKind: ExporterEventKind,eventCode: int,eventMsg: str)
   Notifies the caller that an event occured during the conversion of an assembly.
  
   eventKind: An System.Runtime.InteropServices.ExporterEventKind value indicating the type 
    of event.
  
   eventCode: Indicates extra information about the event.
   eventMsg: A message generated by the event.
  """
  pass
 def ResolveRef(self,assembly):
  """
  ResolveRef(self: ITypeLibExporterNotifySink,assembly: Assembly) -> object
  
   Asks the user to resolve a reference to another assembly.
  
   assembly: The assembly to resolve.
   Returns: The type library for assembly.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
