"""Test for the CCXN class."""

import torch

from topomodelx.nn.cell.ccxn import CCXN


class TestCCXN:
    """Test CCXN."""

    def test_forward(self):
        """Test forward method."""
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = CCXN(
            in_channels_0=2,
            in_channels_1=2,
            in_channels_2=2,
            num_classes=1,
            n_layers=2,
            att=False,
        )

        x_0 = torch.rand(2, 2)
        x_1 = torch.rand(2, 2)

        adjacency_1 = torch.rand(2, 2)
        incidence_2 = torch.rand(2, 2)

        x_0, x_1 = (
            torch.tensor(x_0).float().to(device),
            torch.tensor(x_1).float().to(device),
        )
        adjacency_1 = adjacency_1.float().to(device)
        incidence_2 = incidence_2.float().to(device)

        y = model(x_0, x_1, adjacency_1, incidence_2)
        assert y.shape == torch.Size([1])
