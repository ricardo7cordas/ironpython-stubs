class PlanTopologySet(APIObject, IDisposable, IEnumerable):
    """
    A set that can contain any number of plan topology objects.
    
    PlanTopologySet()
    """
    def Clear(self):
        """
        Clear(self: PlanTopologySet)
            Removes every item from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: PlanTopologySet, item: PlanTopology) -> bool
        
            Tests for the existence of an item within the set.
        
            item: The item to be searched for.
            Returns: The Contains method returns True if the item is within the set, otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PlanTopologySet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: PlanTopologySet, item: PlanTopology) -> int
        
            Removes a specified object from the set.
        
            item: The item to be erased.
            Returns: The number of items that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: PlanTopologySet) -> PlanTopologySetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PlanTopologySet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: PlanTopologySet, item: PlanTopology) -> bool
        
            Insert the specified item into the set.
        
            item: The item to be inserted into the set.
            Returns: Returns whether the item was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: PlanTopologySet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: PlanTopologySet) -> PlanTopologySetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: PlanTopologySet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the set.

Get: Size(self: PlanTopologySet) -> int

"""

