import pytest
from repurp.platform_specs import (
    Platform,
    PlatformSpec,
    platform_specs,
    platforms,
    instagram,
    tiktok,
    twitter,
    linkedin,
    broadcast,
)
from typing import List


def test_platform_specs_structure():
    """Test that platform_specs contains all required platforms with correct structure"""
    assert set(platform_specs.keys()) == set(platforms)
    for platform in platforms:
        assert isinstance(platform_specs[platform], PlatformSpec)


def test_instagram_specs():
    """Test Instagram platform specifications"""
    assert instagram.story == (1080, 1920)
    assert instagram.post == (1080, 1080)
    assert instagram.reel == (1080, 1920)
    assert instagram.max_duration == 60
    assert instagram.bitrate == "4M"
    assert instagram.landscape is None  # Should not have landscape mode


def test_tiktok_specs():
    """Test TikTok platform specifications"""
    assert tiktok.standard == (1080, 1920)
    assert tiktok.max_duration == 180
    assert tiktok.bitrate == "4M"
    assert tiktok.story is None  # Should not have story mode


def test_twitter_specs():
    """Test Twitter platform specifications"""
    assert twitter.landscape == (1920, 1080)
    assert twitter.square == (720, 720)
    assert twitter.max_duration == 140
    assert twitter.bitrate == "2M"
    assert twitter.story is None  # Should not have story mode


def test_linkedin_specs():
    """Test LinkedIn platform specifications"""
    assert linkedin.landscape == (1920, 1080)
    assert linkedin.square == (1080, 1080)
    assert linkedin.max_duration == 600
    assert linkedin.bitrate == "5M"
    assert linkedin.story is None  # Should not have story mode


def test_broadcast_specs():
    """Test Broadcast platform specifications"""
    assert broadcast.standard == (1920, 1080)
    assert broadcast.closeup == (1920, 1080)
    assert broadcast.bitrate == "20M"
    assert broadcast.max_duration is None  # Should not have duration limit
    assert broadcast.story is None  # Should not have story mode


def test_platform_type_validation():
    """Test that Platform type only accepts valid platform names"""
    valid_platforms: List[Platform] = ["instagram", "tiktok", "twitter", "linkedin", "broadcast"]
    
    # This should type check correctly
    for platform in valid_platforms:
        assert platform in platform_specs
        
    # Invalid platforms should raise TypeError at runtime when used with type checking
    with pytest.raises(KeyError):
        _ = platform_specs["invalid_platform"]  # type: ignore
