import unittest
from structural_types import structural_type as struct


class PrimaryNominal(object, struct.StructuralTypeBase):
    """Test class"""
    pass


class SubNominal(PrimaryNominal):
    """Test class"""
    pass


class ValidSubStructuralType(struct.StructuralType):
    """Test class"""

    def __str__(self, *args):
        print(args)


class InvalidSubstructuralType(struct.StructuralType):
    """Test class"""

    random_other_prop = 'Foobar'

    def bad_method(self, *args):
        print(args)


class StructuralTypeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.prim = PrimaryNominal()
        cls.sub = SubNominal()

    def test_basic_substructure(self):
        """Test basic substructure of two classes."""
        self.assertTrue(issubclass(SubNominal, PrimaryNominal))

    def test_invalid_substructure(self):
        """Test invalid substructure of two classes."""
        self.prim.show_class()
        self.sub.show_class()
        with self.assertRaises(AssertionError):
            assert issubclass(struct.StructuralType, InvalidSubstructuralType)

    def test_valid_substructure(self):
        """Test valid substructure of two classes"""
        struct.StructuralType.register(InvalidSubstructuralType)
        struct.StructuralType.register(ValidSubStructuralType)
        # Should work, with valid sub-structural type checking.
        self.assertTrue(
            issubclass(ValidSubStructuralType, struct.StructuralType))
        self.assertFalse(
            issubclass(InvalidSubstructuralType, struct.StructuralType))
