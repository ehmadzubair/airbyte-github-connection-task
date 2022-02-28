GITHUB_STREAMS_DATA = [
    {
        "stream": {
            "name": "commits",
            "jsonSchema": {
                "type": "object",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "properties": {
                    "sha": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "author": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "login": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "gists_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repos_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "avatar_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "site_admin": {
                                "type": [
                                    "null",
                                    "boolean"
                                ]
                            },
                            "gravatar_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "starred_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "followers_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "following_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "organizations_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "subscriptions_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "received_events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "commit": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "tree": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "sha": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "author": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "date": {
                                        "type": [
                                            "null",
                                            "string"
                                        ],
                                        "format": "date-time"
                                    },
                                    "name": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "email": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "message": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "committer": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "date": {
                                        "type": [
                                            "null",
                                            "string"
                                        ],
                                        "format": "date-time"
                                    },
                                    "name": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "email": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "verification": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "reason": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "payload": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "verified": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    },
                                    "signature": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "comment_count": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            }
                        }
                    },
                    "node_id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "parents": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "sha": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "html_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "html_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "committer": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "login": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "gists_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repos_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "avatar_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "site_admin": {
                                "type": [
                                    "null",
                                    "boolean"
                                ]
                            },
                            "gravatar_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "starred_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "followers_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "following_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "organizations_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "subscriptions_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "received_events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "created_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "repository": {
                        "type": [
                            "string"
                        ]
                    },
                    "comments_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                }
            },
            "supportedSyncModes": [
                "full_refresh",
                "incremental"
            ],
            "sourceDefinedCursor": True,
            "defaultCursorField": [
                "created_at"
            ],
            "sourceDefinedPrimaryKey": [
                [
                    "sha"
                ]
            ],
            "namespace": None
        },
        "config": {
            "syncMode": "full_refresh",
            "cursorField": [
                "created_at"
            ],
            "destinationSyncMode": "append",
            "primaryKey": [
                [
                    "sha"
                ]
            ],
            "aliasName": "commits",
            "selected": True
        }
    },
    {
        "stream": {
            "name": "issues",
            "jsonSchema": {
                "type": "object",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "properties": {
                    "id": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "body": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "user": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "login": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "gists_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repos_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "avatar_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "site_admin": {
                                "type": [
                                    "null",
                                    "boolean"
                                ]
                            },
                            "gravatar_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "starred_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "followers_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "following_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "organizations_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "subscriptions_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "received_events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "state": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "title": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "labels": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "id": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "color": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "default": {
                                    "type": [
                                        "null",
                                        "boolean"
                                    ]
                                },
                                "node_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "description": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "locked": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "number": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "node_id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "user_id": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "assignee": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "login": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "gists_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repos_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "avatar_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "site_admin": {
                                "type": [
                                    "null",
                                    "boolean"
                                ]
                            },
                            "gravatar_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "starred_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "followers_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "following_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "organizations_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "subscriptions_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "received_events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "comments": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "html_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "assignees": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "id": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "type": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "login": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "node_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "html_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "gists_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "repos_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "avatar_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "events_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "site_admin": {
                                    "type": [
                                        "null",
                                        "boolean"
                                    ]
                                },
                                "gravatar_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "starred_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "followers_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "following_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "organizations_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscriptions_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "received_events_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "closed_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "milestone": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "state": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "title": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "due_on": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "number": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "creator": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "id": {
                                        "type": [
                                            "null",
                                            "integer"
                                        ]
                                    },
                                    "url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "login": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "node_id": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "html_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "gists_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "repos_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "avatar_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "events_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "site_admin": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    },
                                    "gravatar_id": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "starred_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "followers_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "following_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "organizations_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "subscriptions_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "received_events_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "closed_at": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "created_at": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "labels_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "updated_at": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "description": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "open_issues": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "closed_issues": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            }
                        }
                    },
                    "created_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "events_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "labels_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "repository": {
                        "type": [
                            "string"
                        ]
                    },
                    "updated_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "comments_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "pull_request": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "diff_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "patch_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "repository_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "active_lock_reason": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "author_association": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                }
            },
            "supportedSyncModes": [
                "full_refresh",
                "incremental"
            ],
            "sourceDefinedCursor": True,
            "defaultCursorField": [
                "updated_at"
            ],
            "sourceDefinedPrimaryKey": [
                [
                    "id"
                ]
            ],
            "namespace": None
        },
        "config": {
            "syncMode": "full_refresh",
            "cursorField": [
                "updated_at"
            ],
            "destinationSyncMode": "append",
            "primaryKey": [
                [
                    "id"
                ]
            ],
            "aliasName": "issues",
            "selected": True
        }
    },
    {
        "stream": {
            "name": "pull_requests",
            "jsonSchema": {
                "type": "object",
                "$schema": "http://json-schema.org/draft-07/schema#",
                "properties": {
                    "id": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "base": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "ref": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "sha": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "label": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repo_id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "user_id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            }
                        }
                    },
                    "body": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "head": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "ref": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "sha": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "label": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repo_id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "user_id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            }
                        }
                    },
                    "user": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "login": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "gists_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repos_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "avatar_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "site_admin": {
                                "type": [
                                    "null",
                                    "boolean"
                                ]
                            },
                            "gravatar_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "starred_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "followers_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "following_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "organizations_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "subscriptions_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "received_events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "draft": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "state": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "title": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "_links": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "html": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "self": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "issue": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "commits": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "comments": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "statuses": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "review_comment": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "review_comments": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "href": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "labels": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "id": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "color": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "default": {
                                    "type": [
                                        "null",
                                        "boolean"
                                    ]
                                },
                                "node_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "description": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "locked": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "number": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "node_id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "assignee": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "type": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "login": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "gists_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "repos_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "avatar_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "site_admin": {
                                "type": [
                                    "null",
                                    "boolean"
                                ]
                            },
                            "gravatar_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "starred_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "followers_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "following_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "organizations_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "subscriptions_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "received_events_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "diff_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "html_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "assignees": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "id": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "type": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "login": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "node_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "html_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "gists_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "repos_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "avatar_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "events_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "site_admin": {
                                    "type": [
                                        "null",
                                        "boolean"
                                    ]
                                },
                                "gravatar_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "starred_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "followers_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "following_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "organizations_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscriptions_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "received_events_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "closed_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "issue_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "merged_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "milestone": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "id": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "state": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "title": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "due_on": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "number": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "creator": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "id": {
                                        "type": [
                                            "null",
                                            "integer"
                                        ]
                                    },
                                    "url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "login": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "node_id": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "html_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "gists_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "repos_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "avatar_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "events_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "site_admin": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    },
                                    "gravatar_id": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "starred_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "followers_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "following_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "organizations_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "subscriptions_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "received_events_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "node_id": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "html_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "closed_at": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "created_at": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "labels_url": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "updated_at": {
                                "type": [
                                    "null",
                                    "string"
                                ],
                                "format": "date-time"
                            },
                            "description": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "open_issues": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            },
                            "closed_issues": {
                                "type": [
                                    "null",
                                    "integer"
                                ]
                            }
                        }
                    },
                    "patch_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "auto_merge": {
                        "type": [
                            "null",
                            "object"
                        ],
                        "properties": {
                            "enabled_by": {
                                "type": [
                                    "null",
                                    "object"
                                ],
                                "properties": {
                                    "id": {
                                        "type": [
                                            "null",
                                            "integer"
                                        ]
                                    },
                                    "url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "type": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "login": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "node_id": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "html_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "gists_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "repos_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "avatar_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "events_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "site_admin": {
                                        "type": [
                                            "null",
                                            "boolean"
                                        ]
                                    },
                                    "gravatar_id": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "starred_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "followers_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "following_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "organizations_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "subscriptions_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    },
                                    "received_events_url": {
                                        "type": [
                                            "null",
                                            "string"
                                        ]
                                    }
                                }
                            },
                            "commit_title": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "merge_method": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            },
                            "commit_message": {
                                "type": [
                                    "null",
                                    "string"
                                ]
                            }
                        }
                    },
                    "created_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "repository": {
                        "type": [
                            "string"
                        ]
                    },
                    "updated_at": {
                        "type": [
                            "null",
                            "string"
                        ],
                        "format": "date-time"
                    },
                    "commits_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "comments_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "statuses_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "requested_teams": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "id": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "name": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "slug": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "parent": {
                                    "type": [
                                        "null",
                                        "object"
                                    ],
                                    "properties": {

                                    }
                                },
                                "node_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "privacy": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "html_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "permission": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "description": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "members_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "repositories_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "merge_commit_sha": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "active_lock_reason": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "author_association": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "review_comment_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "requested_reviewers": {
                        "type": [
                            "null",
                            "array"
                        ],
                        "items": {
                            "type": [
                                "null",
                                "object"
                            ],
                            "properties": {
                                "id": {
                                    "type": [
                                        "null",
                                        "integer"
                                    ]
                                },
                                "url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "type": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "login": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "node_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "html_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "gists_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "repos_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "avatar_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "events_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "site_admin": {
                                    "type": [
                                        "null",
                                        "boolean"
                                    ]
                                },
                                "gravatar_id": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "starred_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "followers_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "following_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "organizations_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "subscriptions_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                },
                                "received_events_url": {
                                    "type": [
                                        "null",
                                        "string"
                                    ]
                                }
                            }
                        }
                    },
                    "review_comments_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                }
            },
            "supportedSyncModes": [
                "full_refresh",
                "incremental"
            ],
            "sourceDefinedCursor": True,
            "defaultCursorField": [
                "updated_at"
            ],
            "sourceDefinedPrimaryKey": [
                [
                    "id"
                ]
            ],
            "namespace": None
        },
        "config": {
            "syncMode": "full_refresh",
            "cursorField": [
                "updated_at"
            ],
            "destinationSyncMode": "append",
            "primaryKey": [
                [
                    "id"
                ]
            ],
            "aliasName": "pull_requests",
            "selected": True
        }
    },
    {
        "stream": {
            "name": "users",
            "jsonSchema": {
                "type": [
                    "null",
                    "object"
                ],
                "$schema": "http://json-schema.org/draft-07/schema#",
                "properties": {
                    "id": {
                        "type": [
                            "null",
                            "integer"
                        ]
                    },
                    "url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "type": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "login": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "node_id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "html_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "gists_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "repos_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "avatar_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "events_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "site_admin": {
                        "type": [
                            "null",
                            "boolean"
                        ]
                    },
                    "gravatar_id": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "starred_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "organization": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "followers_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "following_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "organizations_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "subscriptions_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "received_events_url": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                }
            },
            "supportedSyncModes": [
                "full_refresh"
            ],
            "sourceDefinedCursor": None,
            "defaultCursorField": [

            ],
            "sourceDefinedPrimaryKey": [
                [
                    "id"
                ]
            ],
            "namespace": None
        },
        "config": {
            "syncMode": "full_refresh",
            "cursorField": [

            ],
            "destinationSyncMode": "append",
            "primaryKey": [
                [
                    "id"
                ]
            ],
            "aliasName": "users",
            "selected": True
        }
    }
]
